import React from 'react'
import  { createRoot }  from 'react-dom/client';
import textField from "@packages/components/input/textField"

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<textField name="name" id="name" />);