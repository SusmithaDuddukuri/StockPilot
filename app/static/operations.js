(() => {
  'use strict';
  const $ = (selector) => document.querySelector(selector);
  const state = { panel: 'suppliers', cache: {} };
  const panelInfo = {
    suppliers: {title:'Suppliers', kicker:'PARTNERS', description:'Manage vendors and replenishment lead times.', endpoint:'/api/ops/suppliers', columns:[['code','Supplier code'],['name','Supplier'],['contact_name','Contact'],['email','Email'],['lead_days','Lead days'],['active','Status']], action:'New supplier'},
    'purchase-orders': {title:'Purchase orders',kicker:'PROCUREMENT',description:'Track approved orders, expected arrivals and received quantities.',endpoint:'/api/ops/purchase-orders',columns:[['po_number','PO number'],['supplier_name','Supplier'],['status','Status'],['expected_date','Expected'],['line_count','Lines'],['total_cost','Total cost']],action:'New purchase order'},
    receipts:{title:'Receiving',kicker:'INBOUND',description:'Review receipts against purchase orders and stock entries.',endpoint:'/api/ops/receipts',columns:[['receipt_number','Receipt'],['po_number','PO number'],['sku','SKU'],['product_name','Product'],['quantity','Units'],['received_by','Received by'],['created_at','Received at']],action:'Record receipt'},
    transfers:{title:'Stock transfers',kicker:'WAREHOUSE',description:'Review bin-to-bin movements and location changes.',endpoint:'/api/ops/transfers',columns:[['transfer_number','Transfer'],['sku','SKU'],['quantity','Units'],['from_location','From'],['to_location','To'],['status','Status'],['created_at','Created']],action:'New transfer'},
    returns:{title:'Returns',kicker:'REVERSE LOGISTICS',description:'Inspect returned goods and decide whether to restock or scrap.',endpoint:'/api/ops/returns',columns:[['return_number','Return'],['sku','SKU'],['quantity','Units'],['reason','Reason'],['disposition','Disposition'],['status','Status'],['created_at','Opened']],action:'Open return'},
    shipments:{title:'Shipments',kicker:'OUTBOUND',description:'Track carrier handoff and delivery state.',endpoint:'/api/ops/shipments',columns:[['shipment_number','Shipment'],['customer','Customer'],['carrier','Carrier'],['tracking_number','Tracking'],['status','Status'],['shipped_at','Shipped at'],['delivered_at','Delivered at']],action:'New shipment'},
    'cycle-counts':{title:'Cycle counts',kicker:'INVENTORY CONTROL',description:'Reconcile physical stock counts and audit quantity variances.',endpoint:'/api/ops/cycle-counts',columns:[['count_number','Count'],['sku','SKU'],['product_name','Product'],['expected_qty','Expected'],['counted_qty','Counted'],['variance','Variance'],['counted_by','Counted by']],action:'Record count'},
    'reorder-recommendations':{title:'Reorder queue',kicker:'REPLENISHMENT',description:'Prioritize low-stock items with suggested order quantities and estimated cost.',endpoint:'/api/ops/reorder-recommendations',columns:[['sku','SKU'],['name','Product'],['quantity','On hand'],['reorder_level','Reorder point'],['suggested_order','Suggested order'],['estimated_cost','Estimated cost'],['supplier','Supplier']],action:null},
    planning:{title:'Demand planning',kicker:'INVENTORY INTELLIGENCE',description:'Review stock cover, replenishment urgency, ABC value class, and suggested order quantities.',endpoint:'/api/ops/planning/replenishment?horizon_days=14',columns:[['sku','SKU'],['name','Product'],['quantity','On hand'],['lead_days','Lead days'],['days_of_cover','Days of cover'],['target_stock','Target stock'],['suggested_order_qty','Suggested order'],['urgency','Urgency']],action:null},
    audit:{title:'Audit trail',kicker:'GOVERNANCE',description:'Review inventory changes and operational actions in time order.',endpoint:'/api/ops/audit?limit=200',columns:[['created_at','Timestamp'],['event_type','Event'],['entity_type','Entity'],['entity_id','Entity ID'],['summary','Summary'],['actor','Actor']],action:null},
    alerts:{title:'Alert center',kicker:'EXCEPTIONS',description:'Prioritized actions across stock, purchase orders, returns and shipping.',endpoint:'/api/ops/analytics/alerts',columns:[['severity','Severity'],['type','Alert type'],['title','Action required'],['detail','Details'],['reference','Reference']],action:null},
    locations:{title:'Location analysis',kicker:'WAREHOUSE LAYOUT',description:'Compare SKU concentration, stock value and at-risk inventory by location.',endpoint:'/api/ops/analytics/locations',columns:[['location','Location'],['sku_count','SKUs'],['units','Units'],['inventory_value','Inventory value'],['value_share_percent','Value share %'],['at_risk_skus','At-risk SKUs'],['health','Health']],action:null},
    'supplier-scorecards':{title:'Supplier scorecards',kicker:'PROCUREMENT INSIGHTS',description:'Review order completion, overdue purchase orders and receipt activity.',endpoint:'/api/ops/analytics/suppliers',columns:[['code','Code'],['name','Supplier'],['lead_days','Lead days'],['purchase_orders','Orders'],['completed_orders','Completed'],['overdue_orders','Overdue'],['completion_rate','Completion %'],['units_received','Units received'],['rating','Assessment']],action:null},
    'order-analytics':{title:'Order analytics',kicker:'FULFILMENT PERFORMANCE',description:'Track open backlog, ship rate, order status distribution and destination demand.',endpoint:'/api/ops/analytics/orders',columns:[['total_orders','Total orders'],['shipped_orders','Shipped'],['open_orders','Open orders'],['open_units','Open units'],['ship_rate_percent','Ship rate %']],action:null},
    'movement-analytics':{title:'Movement analytics',kicker:'STOCK FLOW',description:'Inspect recent inbound/outbound flow and frequently moved SKUs.',endpoint:'/api/ops/analytics/movement?days=30',columns:[['window_days','Window (days)'],['daily','Daily flow JSON'],['top_movers','Top movers JSON']],action:null},
    'policy-engine':{title:'Operational policy engine',kicker:'CONTROL LIBRARY',description:'Browse executable warehouse control packs covering inventory, receiving, safety, fulfilment and supplier risk.',endpoint:'/api/ops/policies?offset=0&limit=100',columns:[['pack_id','Pack ID'],['module','Rule pack'],['rule_count','Controls'],['scope','Operational scope']],action:null}
  };
  const forms = {
    suppliers:[['code','Supplier code','text',true],['name','Supplier name','text',true],['contact_name','Contact name','text'],['email','Email','email'],['phone','Phone','text'],['lead_days','Lead time (days)','number',true,'7']],
    'purchase-orders':[['po_number','PO number','text',true],['supplier_id','Supplier','supplier',true],['expected_date','Expected date','date'],['notes','Notes','textarea'],['lines','Order line JSON','textarea',true,'[{"sku":"SKU-1042","quantity":10}]']],
    receipts:[['purchase_order_id','Purchase order ID','number',true],['sku','SKU','product',true],['quantity','Quantity received','number',true],['receipt_number','Receipt number','text',true],['received_by','Received by','text'],['note','Note','text']],
    transfers:[['transfer_number','Transfer number','text',true],['sku','SKU','product',true],['quantity','Quantity','number',true],['from_location','Source location','text',true],['to_location','Destination location','text',true],['note','Note','text']],
    returns:[['return_number','Return number','text',true],['sku','SKU','product',true],['quantity','Quantity','number',true],['reason','Reason','text',true],['disposition','Disposition','select',true,['Inspection','Restock','Scrap','Supplier claim']],['customer_name','Customer','text']],
    shipments:[['shipment_number','Shipment number','text',true],['order_id','Order ID (optional)','number'],['carrier','Carrier','text',true],['tracking_number','Tracking number','text']],
    'cycle-counts':[['count_number','Count number','text',true],['sku','SKU','product',true],['counted_qty','Physical quantity','number',true],['counted_by','Counted by','text'],['note','Note','text']]
  };
  const escapeHtml = (value) => String(value ?? '—').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  const format = (key, value) => {
    if (key === 'active') return Number(value) ? '<span class="ops-pill good">Active</span>' : '<span class="ops-pill bad">Inactive</span>';
    if (key === 'status' || key === 'disposition') {
      const v = String(value ?? '—');
      const cls = /received|delivered|restocked|shipped|completed|active/i.test(v) ? 'good' : /open|awaiting|inspection|transit|partial|picking/i.test(v) ? 'warn' : '';
      return `<span class="ops-pill ${cls}">${escapeHtml(v)}</span>`;
    }
    if (key === 'severity') { const v=String(value||'').toLowerCase(); return `<span class="ops-pill ${v==='critical'?'bad':v==='high'?'warn':'good'}">${escapeHtml(value)}</span>`; }
    if (key === 'completion_rate' || key === 'value_share_percent' || key === 'ship_rate_percent') return value == null ? '—' : `${escapeHtml(value)}%`;
    if (key === 'inventory_value' || key === 'total_cost' || key === 'estimated_cost') return value == null ? '—' : `₹${Number(value).toLocaleString('en-IN',{minimumFractionDigits:2,maximumFractionDigits:2})}`;
    if (key === 'variance' && Number(value) !== 0) return `<span class="ops-pill ${Number(value)<0?'bad':'warn'}">${Number(value)>0?'+':''}${escapeHtml(value)}</span>`;
    if (key === 'urgency') { const cls = String(value).toLowerCase(); return `<span class="ops-pill ${cls==='critical'?'bad':cls==='high'?'warn':cls==='normal'?'good':''}">${escapeHtml(value)}</span>`; }
    if (key === 'days_of_cover' && value == null) return 'No demand history';
    return escapeHtml(value);
  };
  async function request(url, options={}) {
    const response = await fetch(url, {headers:{'Content-Type':'application/json',...(options.headers||{})},...options});
    const type = response.headers.get('content-type') || '';
    const data = type.includes('application/json') ? await response.json() : await response.text();
    if (!response.ok) throw new Error(data?.error || `Request failed (${response.status})`);
    return data;
  }
  function notify(message, error=false) {
    const box = $('#ops-notice'); box.className = `ops-notice ${error?'error':'success'}`; box.textContent = message;
    if (!error) setTimeout(() => { if (box.textContent === message) box.textContent = ''; }, 4500);
  }
  function renderTable(info, data) {
    if (!Array.isArray(data) || data.length === 0) return '<div class="ops-empty"><strong>No records yet</strong>New operational records will appear here once created.</div>';
    const head = info.columns.map(([,label])=>`<th>${escapeHtml(label)}</th>`).join('');
    const body = data.map(row=>`<tr>${info.columns.map(([key])=>`<td>${format(key,row[key])}</td>`).join('')}</tr>`).join('');
    return `<table class="ops-table"><thead><tr>${head}</tr></thead><tbody>${body}</tbody></table>`;
  }
  async function loadPanel(panel=state.panel) {
    state.panel = panel;
    const info = panelInfo[panel];
    document.querySelectorAll('[data-panel]').forEach(button=>button.classList.toggle('selected',button.dataset.panel===panel));
    $('#panel-title').textContent = info.title; $('#panel-kicker').textContent = info.kicker; $('#panel-description').textContent = info.description;
    $('#new-record').hidden = !info.action; $('#new-record').textContent = info.action ? `＋ ${info.action}` : 'No action available';
    $('#ops-table-wrap').innerHTML = '<div class="ops-loading">Loading records…</div>';
    try { let data = await request(info.endpoint); if (panel==='alerts') data=data.alerts||[]; else if(panel==='locations') data=data.locations||[]; else if(panel==='supplier-scorecards') data=Array.isArray(data)?data:[]; else if(panel==='order-analytics') data=[data]; else if(panel==='movement-analytics') data=[{window_days:data.window_days,daily:JSON.stringify(data.daily||[]),top_movers:JSON.stringify(data.top_movers||[])}]; else if(panel==='policy-engine') data=data.packs||[]; state.cache[panel]=data; $('#ops-table-wrap').innerHTML=renderTable(info,data); }
    catch (error) { $('#ops-table-wrap').innerHTML=`<div class="ops-empty"><strong>Could not load this view</strong>${escapeHtml(error.message)}<p><button class="ops-button" id="retry-load">Try again</button></p></div>`; $('#retry-load')?.addEventListener('click',()=>loadPanel(panel)); }
  }
  async function loadMetrics() {
    try {
      const [summary] = await Promise.all([request('/api/ops/reports/summary')]);
      const inventory=summary.inventory || {};
      const values=[inventory.sku_count ?? 0,inventory.units ?? 0,summary.returns_open ?? 0,summary.shipments_in_transit ?? 0];
      $('#ops-metrics').querySelectorAll('article strong').forEach((node,index)=>node.textContent=Number(values[index]).toLocaleString('en-IN'));
    } catch (error) { notify(`Metrics unavailable: ${error.message}`,true); }
  }
  function fieldMarkup(field) {
    const [key,label,type,required,extra] = field;
    const req = required ? 'required' : '';
    const full = type==='textarea' || key==='lines' ? ' full' : '';
    if (type==='select') return `<label class="ops-field${full}">${escapeHtml(label)}<select name="${key}" ${req}>${extra.map(x=>`<option>${escapeHtml(x)}</option>`).join('')}</select></label>`;
    if (type==='textarea') return `<label class="ops-field${full}">${escapeHtml(label)}<textarea name="${key}" ${req} placeholder="Enter ${escapeHtml(label.toLowerCase())}">${escapeHtml(extra||'')}</textarea></label>`;
    if (type==='supplier' || type==='product') {
      const options = type==='supplier' ? (state.cache.suppliers||[]).map(x=>`<option value="${x.id}">${escapeHtml(x.code)} · ${escapeHtml(x.name)}</option>`).join('') : [];
      const productOptions = type==='product' ? ((state.cache.products||[]).map(x=>x.sku)).filter(Boolean) : [];
      return `<label class="ops-field${full}">${escapeHtml(label)}${type==='supplier'?`<select name="${key}" ${req}>${options}</select>`:`<input name="${key}" list="product-skus" ${req} placeholder="SKU-1042"><datalist id="product-skus">${[...new Set(productOptions.concat(['SKU-1042','SKU-1088','SKU-1130','SKU-1205','SKU-1266','SKU-1301','SKU-1389','SKU-1414']))].map(x=>`<option value="${escapeHtml(x)}">`).join('')}</datalist>`}</label>`;
    }
    return `<label class="ops-field${full}">${escapeHtml(label)}<input name="${key}" type="${type}" ${req} ${extra && type==='number'?`value="${escapeHtml(extra)}"`:''} ${type==='number'?'min="0"':''} ${key==='expected_date'?'':' '} placeholder="${type==='text'?'Enter '+escapeHtml(label.toLowerCase()):''}"></label>`;
  }
  async function openDialog() {
    const panel=state.panel, info=panelInfo[panel];
    if (!forms[panel]) { notify('This workflow is read-only in this view.',true); return; }
    try {
      if (!state.cache.suppliers) state.cache.suppliers = await request('/api/ops/suppliers');
      if (!state.cache.products) state.cache.products = await request('/api/products');
      if (!state.cache['purchase-orders']) state.cache['purchase-orders'] = await request('/api/ops/purchase-orders');
      $('#dialog-title').textContent=info.action; $('#dialog-fields').innerHTML=forms[panel].map(fieldMarkup).join('');
      $('#record-dialog').showModal();
    } catch (error) { notify(`Could not prepare form: ${error.message}`,true); }
  }
  function closeDialog() { $('#record-dialog').close(); }
  async function saveRecord(event) {
    event.preventDefault();
    const form=$('#record-form'); const data=Object.fromEntries(new FormData(form).entries());
    form.querySelector('[type="submit"]').disabled=true;
    try {
      let endpoint='', method='POST';
      if(state.panel==='suppliers') endpoint='/api/ops/suppliers';
      if(state.panel==='purchase-orders') { endpoint='/api/ops/purchase-orders'; try { data.lines=JSON.parse(data.lines); } catch { throw new Error('Order line JSON must be valid JSON, e.g. [{"sku":"SKU-1042","quantity":10}]'); } data.supplier_id=Number(data.supplier_id); }
      if(state.panel==='receipts') { endpoint=`/api/ops/purchase-orders/${Number(data.purchase_order_id)}/receive`; delete data.purchase_order_id; data.quantity=Number(data.quantity); }
      if(state.panel==='transfers') { endpoint='/api/ops/transfers'; data.quantity=Number(data.quantity); }
      if(state.panel==='returns') { endpoint='/api/ops/returns'; data.quantity=Number(data.quantity); }
      if(state.panel==='shipments') { endpoint='/api/ops/shipments'; if(data.order_id) data.order_id=Number(data.order_id); else delete data.order_id; }
      if(state.panel==='cycle-counts') { endpoint='/api/ops/cycle-counts'; data.counted_qty=Number(data.counted_qty); }
      await request(endpoint,{method,body:JSON.stringify(data)});
      closeDialog(); form.reset(); notify(`${panelInfo[state.panel].title} record saved successfully.`);
      await Promise.all([loadPanel(state.panel),loadMetrics()]);
    } catch(error) { notify(error.message,true); }
    finally { form.querySelector('[type="submit"]').disabled=false; }
  }
  document.querySelectorAll('[data-panel]').forEach(button=>button.addEventListener('click',()=>loadPanel(button.dataset.panel)));
  $('#new-record').addEventListener('click',openDialog); $('#record-form').addEventListener('submit',saveRecord);
  $('#close-dialog').addEventListener('click',closeDialog); $('#cancel-dialog').addEventListener('click',closeDialog);
  $('#refresh-all').addEventListener('click',async()=>{ await Promise.all([loadPanel(),loadMetrics()]); notify('Workspace data refreshed.'); });
  $('#record-dialog').addEventListener('click',event=>{if(event.target===$('#record-dialog'))closeDialog();});
  Promise.all([loadPanel(),loadMetrics()]);
})();
