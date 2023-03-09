import React, { useState } from "react";
import validator from "validator";
import "../Commons.css";
import "./Auth.css";
import Bar from "../Bar";

/**
 * 
 * @param {*} props 
 * Register page qui permet a l'utilisateur de s'inscrire
 * @returns 
 */

export const Register = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [verifpass, setVerifpass] = useState('');
    const [firstname, setFirstname] = useState('');
    const [lastname, setLastname] = useState('');

    const handleSubmit = (event) => {
        if (validator.isEmail(email) === false) {
            alert("Email is not valid");
            return;
        }
        event.preventDefault();
        fetch('http://localhost:8000/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                password: pass,
                first_name: firstname,
                last_name: lastname
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
            if (verifpass !== pass) {
                console.log("Passwords don't match");
                alert("Passwords don't match");
            }
        });
    }
    
    return (
        <header className="App-header">
            <Bar></Bar>
            <div className="auth-form-container">
                    <h2>Register</h2>
                <form className="register-form" onSubmit={handleSubmit}>
                    <label htmlFor="firstname">Firstname</label>
                    <input value={firstname} firstname="firstname" onChange={(e) => setFirstname(e.target.value)} id="firstname" placeholder="Firstname" />
                    <label htmlFor="lastname">Lastname</label>
                    <input value={lastname} lastname="lastname" onChange={(e) => setLastname(e.target.value)} id="lastname" placeholder="Lastname" />
                    <label htmlFor="email">Email</label>
                    <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="youremail@gmail.com" id="email" name="email" />
                    <label htmlFor="password">Password</label>
                    <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                    <label htmlFor="password">Verification password</label>
                    <input value={verifpass} onChange={(e) => setVerifpass(e.target.value)} type="password" placeholder="********" id="verifpass" name="verifpass" />
                    <button onClick={handleSubmit} type="submit">Log In</button>
                </form>
                <button className="link-btn" ><a href="/login" className="link">Already have an account? Login here.</a></button>
            </div>
        </header>
    )
}

export default Register;