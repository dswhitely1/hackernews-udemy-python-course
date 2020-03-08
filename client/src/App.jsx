import React, {useState, useEffect} from 'react';
import axios from 'axios'
import {Grid} from '@material-ui/core'
import HackerNewsCard from './Card';

function App() {
    const [articles, setArticles] = useState([]);

    useEffect(()=> {
        axios.get('http://localhost:5000').then(res => setArticles(res.data)).catch(err => console.log(err.response))
    }, [])

    return (
        <Grid container spacing={2}>
            {articles.map((article, id) => <HackerNewsCard key={id} article={article} />)}
        </Grid>
    )
}

export default App;