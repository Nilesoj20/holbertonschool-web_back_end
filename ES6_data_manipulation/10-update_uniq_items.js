/* function that returns an updated map for all items with an initial quantity of 1 */
const updateUniqueItems = (map) => {
  if (map instanceof Map) {
    for (const [key, value] of map.entries()) {
      if (value === 1) {
        map.set(key, 100);
      }
    }
    return map;
  }
  throw new Error('Cannot process');
};

export default updateUniqueItems;
