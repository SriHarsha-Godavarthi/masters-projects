import React,{useEffect,useState} from "react";

export default function TextField(props){
    const [inputValue,setValue]=useState("")
    useEffect(()=>{

    },[inputValue])
    return(<div>
    <label>{props.name}</label>
    <input type="text" id={props.id}name={props.name} value={inputValue} onChange={(e)=>{setValue(e.target.value)}}/>
    </div>
    );
}

