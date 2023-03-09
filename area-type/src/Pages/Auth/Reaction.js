import React, { useState } from "react";
import "../Commons.css";
import "./Auth.css";
import Bar from "../Bar"

/**
 * 
 * @param {*} props 
 * Reaction page qui affiche toute les reactions disponibles pour l'utilisateur connecté.
 * Permet aussi a l'utilisateur de chosir une reaction pour une area
 * @returns 
 */

export const Reaction = (props) => {
    const [reactions, setReactions] = useState({});
    const handleClick = (reaction) => {
        localStorage.setItem('reaction', JSON.stringify(reaction));
        localStorage.setItem('parameters', JSON.stringify({'parameters': reaction.parameters, 'type': reaction.type}));
    };
    fetch('http://localhost:8000/getreactions/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token ' + JSON.parse(localStorage.getItem('token'))
        },
        body: JSON.stringify({email: JSON.parse(localStorage.getItem('email'))})
    })
    .then(response => response.json())
    .then(data => {
        setReactions(data.reactions);
        console.log(reactions)
    });
    return (
        <header className="App-header">
            <Bar></Bar>
            <div className="auth-form-container">
                <h2>All Reaction</h2>
                <form className="login-form">
                <div>
                    {
                        Object.keys(reactions).map((key) => (
                        <li key={key}>
                            <strong>[{reactions[key].service}] <a href='./option_action' onClick={() => handleClick(reactions[key])}>{reactions[key].title}</a></strong>: {reactions[key].description}
                        </li>
                        ))
                    }
                </div>
                </form>
            </div>
        </header>
    )
}

export default Reaction;