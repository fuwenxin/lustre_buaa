
class Generate():
    def gen_node(self):  # 后续可以添加input
        node_str = '''
        #ifndef _lustre_pre_lustre_H_
        #define _lustre_pre_lustre_H_

        #include "kcg_types.h"

        /* ========================  input structure  ====================== */
        typedef struct { kcg_bool /* X/ */ X; } inC_lustre_pre_lustre;

        /* =====================  no output structure  ====================== */

        /* ========================  context type  ========================= */
        typedef struct {
          /* ---------------------------  outputs  --------------------------- */
          kcg_bool /* Y/ */ Y;
          /* -----------------------  no local probes  ----------------------- */
          /* -----------------------  no local memory  ----------------------- */
          /* -------------------- no sub nodes' contexts  -------------------- */
          /* ----------------- no clocks of observable data ------------------ */
          /* -------------------- (-debug) no assertions  -------------------- */
          /* ------------------- (-debug) local variables -------------------- */
          kcg_bool /* _L5/ */ _L5;
          kcg_bool /* _L8/ */ _L8;            //  add input
        } outC_lustre_pre_lustre;

        /* ===========  node initialization and cycle functions  =========== */
        /* lustre::lustre_pre/ */
        extern void lustre_pre_lustre(
          inC_lustre_pre_lustre *inC,
          outC_lustre_pre_lustre *outC);

        #ifndef KCG_NO_EXTERN_CALL_TO_RESET
        extern void lustre_pre_reset_lustre(outC_lustre_pre_lustre *outC);
        #endif /* KCG_NO_EXTERN_CALL_TO_RESET */

        #ifndef KCG_USER_DEFINED_INIT
        extern void lustre_pre_init_lustre(outC_lustre_pre_lustre *outC);
        #endif /* KCG_USER_DEFINED_INIT */

        #endif
        '''
        return node_str

    def gen_not(self):
        not_str = '''
        #include "kcg_consts.h"
        #include "kcg_sensors.h"
        #include "lustre_pre_lustre.h"

        /* lustre::lustre_pre/ */
        void lustre_pre_lustre(inC_lustre_pre_lustre *inC, outC_lustre_pre_lustre *outC)
        {
          outC->_L5 = inC->X;
          outC->_L8 = !outC->_L5;
          outC->Y = outC->_L8;
        }

        #ifndef KCG_USER_DEFINED_INIT
        void lustre_pre_init_lustre(outC_lustre_pre_lustre *outC)
        {
          outC->_L8 = kcg_true;
          outC->_L5 = kcg_true;
          outC->Y = kcg_true;
        }
        #endif /* KCG_USER_DEFINED_INIT */


        #ifndef KCG_NO_EXTERN_CALL_TO_RESET
        void lustre_pre_reset_lustre(outC_lustre_pre_lustre *outC)
        {
        }
        #endif /* KCG_NO_EXTERN_CALL_TO_RESET */

        '''
        return not_str