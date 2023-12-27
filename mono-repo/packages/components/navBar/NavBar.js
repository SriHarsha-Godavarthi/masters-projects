import React from 'react'
import {Link} from 'react-router-dom'
import "./navBar.css"
export default function NavBar(props){

  return(
    <nav >
      <ul>
    {props.routes.map((routingInfo)=>{
        return <li key={(routingInfo.name+"#"+routingInfo.path)} style={{width:"max-content"}}><Link to={routingInfo.path}>{routingInfo.name}</Link></li>
    })}
    </ul>
    </nav>
  )
}
