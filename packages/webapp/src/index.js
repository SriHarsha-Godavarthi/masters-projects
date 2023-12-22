import React from 'react'
import  { createRoot }  from 'react-dom/client';
// import App from './src/App.js'

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<h1>react app</h1>);