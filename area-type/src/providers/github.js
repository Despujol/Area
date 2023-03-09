import { signInWithPopup, GithubAuthProvider } from "firebase/auth";
import auth from './../firebase';

export const githubLogin = async () => {
    const provider = new GithubAuthProvider();
    provider.addScope('user, read:user, repo');
    
    await signInWithPopup(auth, provider)
    .then((result) => {
        const credential = GithubAuthProvider.credentialFromResult(result);
        const githubUser = result.user;
        console.log(credential);
        console.log(githubUser);
        fetch('http://localhost:8000/github/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: githubUser.providerData[0].email,
                    first_name: githubUser.displayName,
                    last_name: githubUser.displayName,
                    token: credential.accessToken,
                })
        })
        .then(response => response.json())
        .then(data => {
            localStorage.setItem('email', JSON.stringify(data.data.email));
            localStorage.setItem('first_name', JSON.stringify(data.data.first_name));
            localStorage.setItem('token', JSON.stringify(data.data.token));
            console.log("Connected with Github")
            return true;
        })
        .catch(error => {
            console.error('Error:', error);
        })
    }).catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.customData.email;
        const credential = GithubAuthProvider.credentialFromError(error);

        console.log(errorCode, errorMessage, email, credential);
    });
    return false
}

export default githubLogin;