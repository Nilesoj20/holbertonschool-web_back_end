/* function that returns the sum of all student identifiers */
const getStudentIdsSum = (students) => {
  const id = students.reduce(
    (acc, value) => acc + value.id, 0,
  );
  return id;
};

export default getStudentIdsSum;
