package algorithms.Java;

//Picking each element in list and comparing with others to swap places
public class SelectionSort {

    public static void selectionSort(int[] elements) {
        for (int i = 0; i < elements.length-1; i++) {
            int smallestIndex=i;
            for (int j = i+1; j < elements.length; j++) {
                if (elements[j] < elements[smallestIndex]) {
                    smallestIndex = j;
                }
            }

            int tempElem = elements[i];
            elements[i] = elements[smallestIndex];
            elements[smallestIndex] = tempElem;
        }

    }
}
