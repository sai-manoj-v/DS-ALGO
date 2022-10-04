package algorithms.Java;

class BinarySearch {

    public static int findElement(int number, int[] elements) {
        int start = 0, end = elements.length-1, mid = 0; 
        while (start <= end) {
            mid = (start + end)/2;
            if (elements[mid] == number) {
                return mid;
            } else if (number > elements[mid]) {
                start = mid +1;
            } else {
                end = mid -1;
            }
        }
        return -1;
    }

    public static int findElementWithRecursion(int number, int start, int end, int[] elements) {
        int mid = (start + end) / 2;
        if (elements[mid] == number) {
            return mid;
        } else if (number > elements[mid]) {
            return findElementWithRecursion(number, mid+1, end, elements);
        } else {
            return findElementWithRecursion(number, start, mid-1, elements);
        }
    }
}