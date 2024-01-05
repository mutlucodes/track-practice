// Remove Even Numbers Function
export default function removeEvenNumbers(nums) {
    const oddNumbers = [];
    for (let i = 0; i < nums.length; i++) {
        if (!Number.isInteger(nums[i])) {
            throw new Error('Array must contain only integers');
        }
        if (nums[i] % 2 !== 0) {
            oddNumbers.push(nums[i]);
        }
    }
    return oddNumbers;
}