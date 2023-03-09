import React, { useState } from "react";
import { Navigate } from "react-router-dom";
import googleLogin from "../../providers/google";
import microsoftLogin from "../../providers/microsoft";
import githubLogin from "../../providers/github";
import facebookLogin from "../../providers/facebook";
import "../Commons.css";
import "./Auth.css";
import Bar from "../Bar";

/**
 * 
 * @param {*} props 
 * Page de connexion : permet de ce connecter à son compte ou de se connecter avec un compte google, microsoft, github ou facebook
 * @returns 
 */

export const Login = (props) => {
    const [email, setEmail] = useState('');
    const [pass, setPass] = useState('');
    const [isTrue, setIsTrue] = useState(false);

    function resetLocalStorage() {
        localStorage.setItem('email', JSON.stringify({}));
        localStorage.setItem('first_name', JSON.stringify({}));
        localStorage.setItem('token', JSON.stringify({}));
        localStorage.setItem('action', JSON.stringify({}));
        localStorage.setItem('reaction', JSON.stringify({}));
    }

    const handleSubmit = (event) => {
        event.preventDefault();
        fetch('http://localhost:8000/login/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({email: email, password: pass})
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 200) {
                localStorage.setItem('email', JSON.stringify(data.data.email));
                localStorage.setItem('first_name', JSON.stringify(data.data.first_name));
                localStorage.setItem('token', JSON.stringify(data.data.token));
                console.log('Connected');
                setIsTrue(true);
            } else if (data.status === 401){
                console.log(data.error);
            } else {
                console.log('Error: ', data.error);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
    const handleGoogleLogin = async () => {
        resetLocalStorage();
        await googleLogin();
        if (localStorage.getItem('email') !== null)
            setIsTrue(true);
    }
    const handleMicrosoftLogin = async () => {
        resetLocalStorage();
        await microsoftLogin();
        if (localStorage.getItem('email') !== null)
            setIsTrue(true);
    }
    const handleGithubLogin = async () => {
        resetLocalStorage();
        await githubLogin();
        if (localStorage.getItem('email') !== null)
            setIsTrue(true);
    }
    const handleFacebookeLogin = async () => {
        resetLocalStorage();
        await facebookLogin();
        if (localStorage.getItem('email') !== null)
            setIsTrue(true);
    }
    if (isTrue) {
        return <Navigate to="/service" />;
    } else {
    return (
        <header className="App-header">
            <Bar></Bar>
            <div className="auth-form-container">
                <h2>Login</h2>
                <form className="login-form" onSubmit={handleSubmit}>
                    <label htmlFor="email">email</label>
                    <input value={email} onChange={(e) => setEmail(e.target.value)}type="email" placeholder="youremail@gmail.com" id="email" name="email" />
                    <label htmlFor="password">password</label>
                    <input value={pass} onChange={(e) => setPass(e.target.value)} type="password" placeholder="********" id="password" name="password" />
                    <button onClick={handleSubmit} type="submit">Log In</button>
                    <button onClick={handleGoogleLogin} type="button">Log In with Google</button>
                    <button onClick={handleMicrosoftLogin} type="button">Log In with Microsoft</button>
                    <button onClick={handleGithubLogin} type="button">Log In with Github</button>
                    <button onClick={handleFacebookeLogin} type="button">Log In with Facebook</button>
                </form>
                <button className="link-btn" ><a href="/register" className="link">Don't have an account? Register here.</a></button>
            </div>
        </header>
    )
}
}

export default Login;