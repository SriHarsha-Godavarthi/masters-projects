import React from "react";

export default function Projects(props){
    return(
    <div>
    <h2 style={{color: "orange"}}>
        UnderGraduation Projects
    </h2>
    {props.projects.map((project)=>{
        return(
    <section style={{color: "white",fontFamily:"sans-serif",marginLeft:"250px"}}>
     <h3 style={{color: "chartreuse"}}>🛠️{project.title}</h3>
     <h5 style={{color: "aquamarine"}}>{project.technologies}</h5>
     <p>{project.description}</p>
    </section>)
    })}
    </div>
    );
} 