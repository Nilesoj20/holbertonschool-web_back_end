/* function that returns an array of objects that are located in a specific city */
const getStudentsByLocation = (students, city) => {
  const arratyObjec = students.filter((funtion) => funtion.location === city);
  return arratyObjec;
};

export default getStudentsByLocation;
