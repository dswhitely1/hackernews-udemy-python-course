import React from 'react';
import {Grid, Card, CardActions, CardContent, CardHeader, Link, Button, Typography} from '@material-ui/core';
import {makeStyles} from '@material-ui/core/styles';

const useCardStyles = makeStyles(() => ({
    align: {
        textAlign: 'center'
    }
}))
function HackerNewsCard({article}) {
    const classes=useCardStyles();
    return (
        <Grid item xs={12} sm={6} md={4}>
            <Card>
                <CardHeader title={article.title} />
                <CardContent className={classes.align}>
                    <Typography variant='h2'>{`${article.votes} upvotes`}</Typography>
                </CardContent>
                <CardActions>
                    <Button component={Link} target='_blank' href={article.link}>Article</Button>
                </CardActions>
            </Card>
        </Grid>
    )
}

export default HackerNewsCard