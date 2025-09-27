let url = "http://localhost:8000/main?user=pd684_";
let feth = await fetch(url);
let json = await feth.json();

console.log(json.title);
console.log(json.artist);