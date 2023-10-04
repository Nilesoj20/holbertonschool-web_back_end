/*The promise returns an object with status and body attributes*/
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    .catch(() => Error())
    .finally(() => { console.log('Got a response from the API'); });
}
