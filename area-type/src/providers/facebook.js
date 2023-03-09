import { signInWithPopup, FacebookAuthProvider } from "firebase/auth";
import auth from './../firebase';

export const facebookLogin = async () => {
    const provider = new FacebookAuthProvider();
    provider.addScope('user_likes, user_posts');
    await signInWithPopup(auth, provider)
    .then((result) => {
        const credential = FacebookAuthProvider.credentialFromResult(result);
        const facebookUser = result.user;
        console.log(credential);
        console.log(facebookUser);
        fetch('http://localhost:8000/facebook/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: facebookUser.providerData[0].uid,
                    first_name: facebookUser.displayName,
                    last_name: facebookUser.displayName,
                    token: credential.accessToken,
                })
        })
        .then(response => response.json())
        .then(data => {
            localStorage.setItem('email', JSON.stringify(data.data.email));
            localStorage.setItem('first_name', JSON.stringify(data.data.first_name));
            localStorage.setItem('token', JSON.stringify(data.data.token));
            console.log("Connected with Facebook")
            return true;
        })
        .catch(error => {
            console.error('Error:', error);
        })
    })
    .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        const email = error.customData.email;
        const credential = FacebookAuthProvider.credentialFromError(error);
        console.log(errorCode, errorMessage, email, credential);
    });
}

export default facebookLogin;