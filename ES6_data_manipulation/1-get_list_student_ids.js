/* function that returns an array with the identifiers of a list of objects */
const getListStudentIds = (myArray) => {
  if (!Array.isArray(myArray)) {
    return [];
  }
  return myArray.map((studentId) => studentId.id);
};

export default getListStudentIds;
