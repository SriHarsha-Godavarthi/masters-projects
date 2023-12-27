import React,{useState} from "react";
// import {createBrowserRouter,RouterProvider} from "react-router-dom";
import NavBar from "@packages/components/navBar/NavBar";
import Home from "../pages/Home";
import Error from "../pages/Error";
import { BrowserRouter, Route,Routes } from "react-router-dom";
let routesInfo=[
    {path: "/" ,element: <Home/>,errorElement: <Error/>,name:"Home"},
    {path: "/index" ,element: <Home/>,errorElement: <Error/>,name:"Main"},
]
export default function App(props){

    return(
    <React.StrictMode>
    <BrowserRouter >
    <NavBar routes={routesInfo}/>
    <Routes>
      {routesInfo.map((route)=>{
        return <Route key={route.path} path={route.path} element={route.element}/>})}
    </Routes>
    </BrowserRouter>
    </React.StrictMode>
    )
}