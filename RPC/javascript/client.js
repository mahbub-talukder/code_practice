const jsonrpc = require('jsonrpc-lite');
const http = require('http');

const params = [5, 3];
const payload = jsonrpc.request(1, 'addNumbers', { params });

const options = {
  hostname: 'localhost',
  port: 3000,
  path: '/',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
};

const req = http.request(options, (res) => {
  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    const response = jsonrpc.parse(data);

    if (response.type === 'success') {
      console.log('Result:', response.payload.result);
    } else {
      console.error('Error:', response.payload.error);
    }
  });
});

req.write(JSON.stringify(payload));
req.end();
