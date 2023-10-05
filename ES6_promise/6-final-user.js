/*function that receives 3 arguments and returns Promise with an array*/
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const prom1 = signUpUser(firstName, lastName);
  const prom2 = uploadPhoto(fileName);

  return Promise.allSettled([prom1, prom2]).then((values) => {
    const res = [];
    values.forEach((element) => {
      if (element.status === 'fulfilled') {
        res.push({ status: element.status, value: element.value });
      } else {
        res.push({ status: element.status, value: `${element.reason}` });
      }
    });
    return res;
  });
}
