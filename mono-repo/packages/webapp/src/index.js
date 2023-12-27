import React from 'react'
import  { createRoot }  from 'react-dom/client';
import TextField from "@packages/components/textField/TextField"

const container = document.getElementById('root');
const root = createRoot(container);
// root.render(<TextField id="textfield" name="name"/>);
root.render(<h1>this is my portfolio </h1>)