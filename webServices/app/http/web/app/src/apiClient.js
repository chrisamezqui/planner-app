import axios from 'axios';

const BASE_URI = 'http://localhost:8080';

const client = axios.create({
 baseURL: BASE_URI,
 json: true
});

class APIClient {
 constructor(accessToken) {
   this.accessToken = accessToken;
 }

 createStickynote(postData) {
   return this.perform('post', '/stickynoteIndex', postData);
 }

 deleteStickynote(postData) {
   return this.perform('delete', `/stickynoteIndex/${postData.id}`);
 }

 getAllStickynotes() {
   return this.perform('get', '/stickynoteIndex');
 }

 async perform (method, resource, data) {
   return client({
     method,
     url: resource,
     data,
     headers: {
       Authorization: `Bearer ${this.accessToken}`
     }
   }).then(resp => {
     return resp.data ? resp.data : [];
   })
 }
}

export default APIClient;
