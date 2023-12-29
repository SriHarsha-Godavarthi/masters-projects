import React,{useState} from "react";
// all custom components are imported here
import {NavBar} from "@packages/components/index";
import { Home,Error,Projects } from "../pages/index";
import { BrowserRouter, Route,Routes } from "react-router-dom";
// import "./App.css"

const linkedInUrl="https://www.linkedin.com/in/sri-harsha-godavarthi-2895a0185/"
const githubUrl="https://github.com/SriHarsha-Godavarthi"
const instaGram="https://www.instagram.com/harsha_godavarthi/"

const projectsList=[
    {title:"Face Recognition",
    technologies: "#python#opencv#haar cascade classifier(for classifying images)",
    description:"Face detection used for doing surveillance which will recognize the face and displays name of the person if already have the faceData"},
    {title:"Sentiment Analysis Using Contextual Approach On E-Commerce Reviews" ,
    technologies: "#ML#python",
    description:"Compared performance of machine Learning Algorithms based on contextual approach"}
]


let routesInfo=[
    {path: "/" ,element: <Home/>,errorElement: <Error/>,name:"Home"},
    // {path: "/about" ,element: <Home/>,errorElement: <Error/>,name:"About"},
    // {path: "/contact" ,element: <Home/>,errorElement: <Error/>,name:"Contact"},
    {path: "/projects" ,element: <Projects projects={projectsList}/>,errorElement: <Error/>,name:"Projects"}
]
export default function App(props){
    const [projects,setProjects]=useState(projectsList)
    return(
    <div className="App">
    <BrowserRouter >
    <NavBar routes={routesInfo} linkedInUrl={linkedInUrl} githubUrl={githubUrl} instaGram={instaGram}/>
    <Routes>
      {routesInfo.map((route)=>{
        return <Route key={route.path} path={route.path} element={route.element} errorElement={route.errorElement}/>})}
    </Routes>
    </BrowserRouter>
    </div>
    )
}