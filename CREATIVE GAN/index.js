const fs = require('fs');
const http = require('http');
const url = require('url');
const superagent = require('superagent');

const tempHome = fs.readFileSync('./templates/home.html', 'utf-8');
const tempAbout = fs.readFileSync('./templates/about.html', 'utf-8');
const tempHelp = fs.readFileSync('./templates/help.html', 'utf-8');

const data = fs.readFileSync('./data.json', 'utf-8');
const imgData = JSON.parse(data);

///////SERVER
const server = http.createServer((req, res) => {
  const pathName = req.url;

  if (pathName === '/overview' || pathName === '/') {
    res.end(tempHome);
  } else if (pathName === '/about') {
    res.end(tempAbout);
  } else if (pathName === '/help') {
    res.end(tempHelp);
  } else if (pathName === '/generate') {
    res.writeHead(200, {
      'Content-type': 'text/html',
    });

    superagent.get('https://dog.ceo/api/breeds/image/random').end((err, res) => {
      res.end(`${res.body.message}`);
    });
  } else {
    res.writeHead(404, {
      'Content-type': 'text/html',
    });
    res.end('<h1>Page not found || Invalid url</h1>');
  }
});

server.listen(8000, '127.0.0.1', () => {
  console.log('Listening to requests on port 8000');
});
