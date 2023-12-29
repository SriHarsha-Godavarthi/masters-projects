import React from "react";
import ProfilePic from "@packages/components/images/ProfilePic.png"
export default function Home (props){
        return(
      <div>
        <span style={{display: "flex",justifyContent: "center"}}>
        <img src={ProfilePic} style={{height: "220px",marginLeft:"200px"}} alt='ProfilePic'></img>
        </span>
        <span>
        <h3 style={{color: "orange",fontFamily:"sans-serif",marginLeft:"250px"}}>Hi, i'm Sri Harsha Godavarthi</h3>
        <h2 style={{color: "aquamarine",fontFamily:"sans-serif",marginLeft:"250px"}}>🚀Full Stack Developer🚀</h2>
        <p style={{color: "white",fontFamily:"sans-serif",marginLeft:"600px"}}>
        <h3 style={{color:"aquamarine"}}>About Me</h3>
        Passionate Full Stack Developer with work experience of 1.8 years. 
        In addition to my strong backend abilities in Node.js frameworks (HapiJs, Express Js), Python, and 
        writing test cases for APIs, I contribute knowledge in frontend technologies such as React, HTML, 
        Babel, webPack, Material UI, ES6, and Javascript. I'm excited to adopt new technology and keep up with business trends, and I do well in fast-paced settings. If you're looking for a 
        flexible developer committed to doing excellent work and helping your team succeed, let's get in touch. 
        </p>
        <p style={{color: "lightskyblue",fontFamily:"sans-serif",marginLeft:"600px"}}>
        #WebDevelopment #JavaScript #React #NodeJS #Python #MySQL #NoSQL #FullStackDeveloper
        </p>
        <p style={{color: "white",fontFamily:"sans-serif",marginLeft:"100px"}}>
        <h3 style={{color:"aquamarine"}}>Contact Info</h3>
        <p style={{maxWidth: "180px"}}>310 S Kendall Ave, Apt: 23, Kalamazoo, MI, 49006, United States</p>
        <p> sriharsha.godavarthi@wmich.edu<br></br>(269)-207-9923</p>
        <label></label>
        </p>
        </span>
    
       </div>
        )
}
