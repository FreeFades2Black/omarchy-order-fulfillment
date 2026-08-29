from fastapi import FastAPI
app = FastAPI(title='Order Fulfillment')
@app.get('/health')
def h(): return {'service': 'fulfillment', 'status': 'ok'}
@app.post('/api/orders/dispatch')
def d(): return {'dispatch_id': 'dsp_88192', 'carrier': 'EXPRESS_CARGO'}
