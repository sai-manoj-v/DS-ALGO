package algorithms.Python;

import java.util.Arrays;


//WIP
public class StableMatch {
    
    static int personsCount = 4; // represents number of men and women

    static boolean doesWomenPreferM1OverM(int womenPreferences[][], int women, int men, int newMen) {
        for (int i = 0; i < personsCount; i++) {
            if (womenPreferences[women][i] == newMen) {
                return true;
            }
            if (womenPreferences[women][i] == men) 
                return false;
        }
        return false;
    }

    /*
        Since the method takes all the preferences in one variables
        indexes of men are till personsCount and the indexes of 
        women start from index personCount and range till 2*personsCount-1
    */
    static void stableMatch(int combinedPreferences[][]) {
        int womenPartner[] = new int[personsCount];
        boolean isMenFree[] = new boolean[personsCount];
        int freeMenCount = 0;
        
        Arrays.fill(womenPartner, -1);

        while (freeMenCount > 0) {
            
            //Choosing a free man
            int men; 
            for (men = 0; men < personsCount; men++) {
                if (isMenFree[men] == true) {
                    break; 
                }
            }

            //
            for (int i = 0; i < personsCount && isMenFree[men] == true; i++) {
                int women = combinedPreferences[men][i];
                
                //Asssigning women partner if she's free
                if (womenPartner[women - personsCount] == -1) {
                    womenPartner[women - personsCount] = men;
                    isMenFree[men] = false;
                    freeMenCount--;
                } else {
                    int m1 = womenPartner[women - personsCount];
                    if (doesWomenPreferM1OverM(combinedPreferences, women, m1, men) == false) {
                        womenPartner[women - personsCount] = men;
                        isMenFree[men] = false;
                        isMenFree[m1] = true;
                    }
                }

                

            }


        }
    }
}
