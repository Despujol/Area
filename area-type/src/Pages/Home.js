import './Commons.css';

/**
 * Page d'accueil qui redirige vers le login ou le register
 * @returns 
 */

const Home = () => {
  return (
    <header className="App-header">
    <div class="container"><div class="block-1"><a href='/' className='link'>Area-Type</a></div>
      <div class="block-2"><a href='/login' className='link'>Log in</a></div>
      <div class="block-3"><a href='/register' className='link'>Sign Up</a></div>
  </div>
  <div className='center'>
      <h1>On fait des trucs avec des if et ça fais des else.</h1>
  </div>
  <div className='center'>
      <h1>Essaye avec tes applis preferées et regarde ce qu'il se passe</h1>
  </div>
  <div className='center'>
    <button><a href='/register' className='link'>tu veux essayer ?</a></button>
  </div>
</header>
  )
};

export default Home;
