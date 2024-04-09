const { MongoClient } = require('mongodb');
require('dotenv').config();  //red .env file

console.log(process.env.MONGO_URI);  //test to see if the uri is correcty read or not (it needs to be on the same level)

console.log(typeof process.env.MONGO_URI);  //string

databaseName = "codebase-understanding";
databaseFlags = "?retryWrites=true&w=majority";

connectionURI = process.env.MONGO_URI + databaseName + databaseFlags;  //this will connect everything together through string concanctenation
console.log(connectionURI);  //test to see if the uri is correcty read or not 


async function main() {
    const client = new MongoClient(connectionURI);  //create a new client

    try {
        //connect to the MongoDB cluster
        await client.connect();

        //make the appropriate DB calls
        await listDatabases(client);
        console.log("Successfull connection to the database");
    } catch (e) {
        console.error(e);
    } finally {
        await client.close();
        console.log("Closed connection to the database");
    }
} 

//define the logic for listing the databases in our cluster
async function listDatabases(client) {
    databasesList = await client.db().admin().listDatabases();  //listDatabases() is a method that returns a promise
    console.log("Databases:");
    databasesList.databases.forEach(db => console.log(` - ${db.name}`));  //list out the name of the individual databses that are part of the list

}
main().catch(console.error);