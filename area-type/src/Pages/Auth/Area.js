import React, { useState } from "react";
import "../Commons.css";
import "./Auth.css";
import Bar from "../Bar";

/**
 * 
 * @param {*} props 
 * Area page qui affiche toute les areas disponibles pour l'utilisateur connecté.
 * Permet aussi a l'utilisateur de créer une area avec les actions et reactions qu'il a choisi
 * @returns 
 */

export const Area = (props) => {
    const [area, setArea] = useState({});
    var action = JSON.parse(localStorage.getItem('action')) ?? {};
    var reaction = JSON.parse(localStorage.getItem('reaction')) ?? {};

    console.log(action);
    console.log(reaction);

    const handleSubmit = (event) => {
        fetch('http://localhost:8000/createarea/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
            },
            body: JSON.stringify({
                email: JSON.parse(localStorage.getItem('email')),
                action: action,
                reaction: reaction
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
    };

    fetch('http://localhost:8000/getuseractreact/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        },
        body: JSON.stringify({email: JSON.parse(localStorage.getItem('email'))})

    })
    .then(response => response.json())
    .then(data => {
        setArea(data.data);
    });

    return (
        <header className="App-header">
            <Bar></Bar>
            <div className="auth-form-container">
                <h2>If this {action.title ? action.title : <a href='/action'>add</a>}</h2>
                <h2>Then that {reaction.title ? reaction.title : <a href='/reaction'>add</a>}</h2>
            </div>
            <button className="btn" onClick={handleSubmit}>Submit</button>
            <ul>
                    {
                        Object.keys(area).map((key) => (
                        <li key={key}>
                            <strong>WHEN {area[key].action_title}, DO {area[key].reaction_title}</strong>
                        </li>
                        ))
                    }
                </ul>
        </header>
    )
}

export default Area;
