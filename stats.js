
const { MongoClient } = require('mongodb');

password = `KCT!jfy-cae5vyx1qxb`

const uri = `mongodb+srv://KdZ-site:${password}@cluster0.crjgl.mongodb.net/Project 0?retryWrites=true&w=majority`;

const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

client.connect(err => {
    const collection = client.db("test").collection("devices");
    // perform actions on the collection object
    client.close();
});

console.log(window.location.href);

// window.location.href
