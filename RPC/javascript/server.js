const jsonrpc = require('jsonrpc-lite');
const http = require('http');

const server = http.createServer((req, res) => {
  let data = '';

  req.on('data', chunk => {
    data += chunk;
  });

  req.on('end', () => {
    const request = jsonrpc.parse(data);

    if (request.type === 'request' && request.payload.method === 'addNumbers') {
      const params = request.payload.params;
      const result = params[0] + params[1];

      const response = jsonrpc.success(request.payload.id, result);
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(response));
    } else {
      res.writeHead(400, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(jsonrpc.error(request.payload.id, new jsonrpc.JsonRpcError('Invalid request'))));
    }
  });
});

const port = 3000;
server.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
