import React from 'react'
import {Link} from 'react-router-dom'
import "./navBar.css"
import LinkedInLogo from "../images/linkedInLogo.png";
import GitHub from "../images/githubLogo.png"
import InstaLogo from "../images/instaLogo.png"
export default function NavBar(props){

  const navigateToNewWindow=(e,url)=>{
    var newWindow = window.open(url);
  }
  return(
    <nav >
      <ul>
    {props.routes.map((routingInfo)=>{
        return <li key={(routingInfo.name+"#"+routingInfo.path)} style={{width:"max-content"}}><Link to={routingInfo.path}>{routingInfo.name}</Link></li>
    })}
    </ul>
    <img src={LinkedInLogo} style={{height:"25px",marginRight:"20px"}} alt='linkedin' onClick={(e)=>{navigateToNewWindow(e,props.linkedInUrl)}}></img>
    <img src={GitHub} style={{height:"25px",marginRight:"20px"}} alt='github' onClick={(e)=>{navigateToNewWindow(e,props.linkedInUrl)}}></img>
    <img src={InstaLogo} style={{height:"25px",marginRight:"20px"}} alt='instagram' onClick={(e)=>{navigateToNewWindow(e,props.instaGram)}}></img>
    </nav>
  )
}
