import React from 'react';
import './App.css';

function App() {

  const [Hashvalue, setHashValue] = React.useState('');
  const [fetchData, setFetchedData] = React.useState('');
  const [connectWallet, setConnectWallet] = React.useState('');
  const [walletId, setWalletId] = React.useState(connectWallet)
  const [check, setCheck] = React.useState(0);

  React.useEffect(() => {

    if (typeof window.ethereum === 'undefined') {
      setConnectWallet('MetaMask isnt installed, please install it')
      return false
    }

  }, [connectWallet])


  async function connectWalletwithMetaMask() {
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
    .catch((e) => {
    console.error(e.message)
    return
    })

    if (!accounts) { return }

    console.log(accounts)
    window.userWalletAddress = accounts[0]
    setWalletId(window.userWalletAddress)

    return;

  }

  const getData = async (e) => {


    try {
      e.preventDefault();


      console.log("checked")

      let data;

      if(check === 0){

        data = await fetch(`http://localhost:5000/api/block/number/${Hashvalue}`, {
          method: 'GET',
          // mode:'cors',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }

        });

      }
      else if(check === 1){

        data = await fetch(`http://localhost:5000/api/block/hash/${Hashvalue}`, {
          method: 'GET',
          // mode:'cors',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }

        });
      }
      else if(check === 2){

        data = await fetch(`http://localhost:5000/api/block/transaction_hash/${Hashvalue}`, {
          method: 'GET',
          // mode:'cors',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }

        });
      }
      else{

        data = await fetch(`http://localhost:5000/api/balance/${Hashvalue}`, {
          method: 'GET',
          // mode:'cors',
          headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
          }

        });
      }
      
      

      const response = await data.json();

      if(data.status !== 200){

        const error = response;
        throw error;
    }

      if(!response){
        
        setFetchedData("No Data Recieved");
        return;
      }

      setFetchedData(response);

    } catch (error) {
      
      setFetchedData(error);
    }
    
  }

  return (
    <>
      <div className={`flex flex-wrap main`}>

      <div className='flex flex-column flex-justify-center flex-align-center'>

        <h1>Blockchain Explorer</h1>
        <hr />

        <div className="flex flex-justify-saround">
          <button className='options' onClick={() => setCheck(0)}>Block Number</button>
          <button className='options' onClick={() => setCheck(1)}>Block Hash</button>
        </div>
        
        <button className='options' onClick={() => setCheck(2)}>Transaction Hash</button>
        <button className='options' onClick={() => setCheck(3)}>Metamask Address</button>

        <form onSubmit={getData}>

          <div className="flex flex-column form_div">

            <input className='text_field' type="text" value={Hashvalue} onChange={e => setHashValue(e.target.value)} placeholder={check === 0 ? "Enter Block Number" : check === 1 ? "Enter Block Hash" : check === 2 ? "Enter Transction Hash" : "Enter metamask address"} />
            <input className='btn' type="submit" value="SUBMIT" />

          </div>

        </form>

        <span style={{fontWeight: 500}}>{check === 0 ? 'You are fetching Block Data using Block Number' : check === 1 ? 'You are fetching Block Data using Block Hash' : check === 2 ? 'You are fetching Transaction Data using Transaction Hash' : 'You are fetching Wallet Balance using metamask address'}</span>

        <br />
        <button className='options' style={{background: 'orange'}} onClick={() => connectWalletwithMetaMask()}> Connect Metamask</button>
        {walletId!=='' && <span>Wallet Address: {walletId}</span>}
        <hr />
        <strong><i><span style={{margin: '50px 0 10px 0'}}>CREDIT: ADITYA CHOUHAN</span></i></strong>

      </div>
      <div className='flex Container_2 flex-column'>

        <h2 style={{textAlign: 'center'}}>OUTPUT</h2>
        <div style={{width: '100%'}}>
          <span>{check === 3 ? `Account Balance: ${fetchData}`: fetchData}</span>
        </div>
      </div>

    </div>
    </>
  );
}

export default App;
