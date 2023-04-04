import "node-fetch" as fetch;
// const fetch = require('node-fetch');
const fs = require('fs');
const { promisify } = require('util');
const readFileAsync = promisify(fs.readFile);
const base64 = require('base64-js');

const api_url = 'https://api.imgbb.com/1/upload';
const api_key = 'a431b34dd132a00c26e44d1988330ac0';

async function uploadImage() {
   try {
      const imageData = await readFileAsync('1.jpg');
      const encodedImageData = base64.fromByteArray(imageData);
      const response = await fetch(api_url, {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json'
         },
         body: JSON.stringify({
            key: api_key,
            image: encodedImageData,
            name: 'image.jpg'
         })
      });
      const responseData = await response.json();
      if (response.ok) {
         console.log(responseData.data.url);
      } else {
         console.log(`Error: ${responseData.error}`);
      }
   } catch (error) {
      console.log(`Error: ${error}`);
   }
}

uploadImage();
