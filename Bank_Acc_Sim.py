import random
class BankAccount():
    def __init__(self,name,balance):
        self.balance = balance
        self.name = name
        self.auth = int(raw_input("Enter a 4-Digit PIN for your account : "))
        self.statement ="Initial Balance :",self.balance
        self.anum = random.randint(0,100000)
        self.debt = 0
        print "Bank Account created successfully for",self.name,"with balance",self.balance,"And account number", self.anum

    def deposit(self,deposit):
        self.balance += deposit
        self.statement += "Deposited :", deposit
        print deposit,"deposited to",self.name,"'s Account"
        print "Current Balance is",self.balance        

    def withdraw(self,amount):
        if amount >= self.balance :
            print "Sorry, you have insufficient funds"         else :
            pin1 = int(raw_input("Enter your PIN : "))
            if pin1 == self.auth :
                self.balance -= amount
                self.statement += "Withdrawn :",amount
                print "After this operation your balance is:",self.balance

            else :
                print "Authentication Failed..."

    def loan(self,amount):
        rate = 0
        if amount <= 50000 :
            rate = 6
        elif amount > 50000 & amount < 100000 :
            rate = 8.5
        elif amount > 100000 :
            rate = 11
        self.debt += amount
        self.statement += "Loan Approved :",amount
        print "Your loan of",amount,"has been approved at a rate of",rate,"% per annum"

    def statement(self):
        print "" + self.statement
        print "Balance :",self.balance

    def __del__(self):

        print "Your account has been submitted for closure. Thank you for banking with us."

#----------------Class Definition Ends here----------------

def acc_init():
    init_name=raw_input("Enter your name here : ")
    init_bal = raw_input (" Enter starting balance : ")
    init_name = raw_input("Input any name to use as object name : ")
    init_name = BankAccount(init_name,init_balance)

def acc_dep():
    dep_amount=float(raw_input("Enter amount to be deposited into the account")
    



def main():
    print 'Welcome to ABC Bank'

    print 'What do you want to do ?'

    print '1. Open a new account'
    print '2. Deposit Money into an account'
    print '3. Withdraw Money from your account'
    print '4. Take a loan'
    print '5. Generate a statement'
age = int(raw_input("Enter your age to verify :"))
if age => 18 :
    print 'Sir you are eligible to create the account '
else:
    print 'Sorry sir you cannot create an account '
t = terms

print 'Sir according to our policy you have to accept our terms and conditions:'
print """Terms and Conditions of Current Account
These terms and conditions apply to and regulate the operation of the Current Account (the
“Current Account/s”) offered by ICICI Bank Limited (the “Bank”) to Customers. Various Current
Account Products offered by the Bank . These terms and conditions (“Terms) shall be in addition
and subject to any other terms as stipulated by the Bank from time to time.
1. Definitions:
In these terms and conditions, the following words and phrases have the meaning stated
hereunder unless indicated otherwise:
a) “Account” refers to the Current Account that may be opened and held with an eBoR
branch
b) “Account Opening Form” (AOF) refers to the respective relationship forms for Current
Account products available for eBOR customer's.
c) “Customer" refers to any person holding an Account with an eBoR branch.
d) “Month" shall mean a month reckoned according to the British calendar.
e) “Quarter” shall mean a financial quarter i.e. April – June, July –September, October –
December, January – March in any financial year.
f) “Services" shall mean the various services that may be provided by eBoR branches in
connection with the Account and are more particularly referred to / described in these
Terms and/or on the website.
g) “Services Directory” shall mean and include the media by which details about the
charges
and the rates at which the services are provided for the respective types of Account
available for eBOR customer's.
h) “Website" refers to the website owned, established and maintained by ICICI Bank at the
URL www.bankofrajasthan.com
i) “eBoR” shall mean erstwhile Bank of Rajasthan.
Interpretation:
a) All references to singular include plural and vice versa and the word "includes" should be
construed as "without limitation".
b) Words importing any gender include the other gender.
c) Reference to any statute, ordinance or other law includes all regulations and other
instruments and all consolidations, amendments, re-enactments or replacements for the
time being in force.
d) All headings, bold typing and italics (if any) have been inserted for convenience of
reference only and do not define limit or affect the meaning or interpretation of these
Terms.
e) Words “ICICI Bank”, “the Bank”, refer to ICICI Bank Limited, having its registered office at
Landmark, Race Course Circle, Vadodara -390007.
2. Applicability of Terms:
The terms and conditions (“Terms”) set out below, together with the AOF, account charges
and any other conditions which may be implied by law shall govern the operation of the
1
current account and other related services offered by eBoR branches to the Customer. By
applying for opening the Account, the Customer acknowledges that he / she has read,
understood and accepted these terms and conditions, which form a part of the Customer’s
application to the Bank.
3. Account Opening:
The Account opening formalities are governed by the policies of eBoR branches and may
be revised from time to time. The Bank may require Customer/s to submit duly filled
application form/s along with the prescribed set of documents stipulated from time to time,
to the satisfaction of the Bank.
An individual or a firm should have only one Account and should disclose details of other
accounts with other branches/banks.
4. Operating Accounts:
An Account may be opened in the names of:
a) An individual in his / her own name;
b) Two or more individuals having contractual capacity may open a joint account in their
names.
c) Sole-Proprietorship Firms, Partnership Firms, Limited companies, Hindu Undivided
Family Firms, Trusts, Executors / Administrators, Government / Semi-Government / Local
Bodies, Associations, Societies, Liquidators, Receivers, Agents on behalf of Principals,
Accounts (and related Services availed of from time to time) in the names of a company,
partnership firm, trust, association or other entity shall be operated by the authorised
signatory(ies) of the respective entities, as specified in the AOF / resolution submitted by
such entity at the time of opening the Account or as varied in accordance with these terms
and conditions. Changes to authorised signatories of such entities shall be recognised only
upon due submission of the requisite authorizations / resolutions approving such changes,
to the satisfaction of the eBoR branch.
4.1 While opening joint accounts, clear mandate regarding operations in the account
should be provided. Such mandate may be one of the following :
(i) operation jointly by all persons.
(ii) operation by two or more persons jointly.
(iii) operation by either of them.
(iv) operation by either or survivor.
(v) operation by former or survivor/s.
4.2 It should, however, be noted that the mandate, other than “Operations Jointly by all”
given by the account holders is valid only for the normal / ordinary transactions in the
account. For exceptional transactions, consent from all the joint account holders is
necessary. Deposit of amount and withdrawal of amount in a deposit account or taking
payment of Term Deposit on or after maturity are regarded as normal transactions.
Opening of account, closing of account, loan/ overdraft against deposits, pre-mature
payment of term deposits, lodging security for advance and / or taking delivery of security
2
after adjustment of advance are exceptional transactions for which consent of all the
depositors is necessary. The consent of all the depositors should be provided either at the
time of opening of the account or as & when there is a request for such transactions.
4.3 Further the mandate given by the joint account holders is valid during the life time of all
the joint account holders unless a contrary intention is apparent. Thus, the mandate to
permit operations in the account “by either of us” or “by any two (out of more than two) of
us” will stand terminated upon death of any of the joint account holders. But in case the
mandate permits operations in the account by “Either or Survivor/s ” or “Former or
Survivor/s” the balance in the account can be paid to survivor/s after death of one of the
joint account holders. However, loan against term deposits and / or before maturity
payment of term deposits are not covered by such mandate.
4.4 Joint account – operation jointly by all persons
4.4.1 In such accounts, the names in the title of the account shall be connected with
conjunction ‘AND’ as “Mr. Akash AND Kartik”. The cheques / withdrawal slips should be
signed by all the account holders.
4.4.2 Upon death, insolvency or lunacy of any of joint account holders, further
operations in the account shall be stopped.
4.5 Joint Accounts – Operation by Either or Survivor
In such cases the names shall be connected with conjunction ‘or’ as ‘Akash or Kartik’. The
cheques / contingent cheques / withdrawal slips may be drawn by any one of the account
holders.
4.6 Joint Accounts – Operation by “Former or Survivor”
4.6.1 In case an Account is opened with the instructions for operation by “Former or
Survivor”, the intention of the owner (former) depositor is to retain all rights with himself
during his life time and to facilitate the repayment of balance lying in the account to the
survivor after his death. Accordingly during his life time, he can operate his SB and Current
Deposit Account and can take before maturity payment of term deposit or loan against
term deposit without consent of other depositors. He can even close his deposit account
without the consent of other depositors.
4.6.2 It is only after the death of the former that the survivor/s is / are entitled to take
repayment of balance lying in Savings Bank Account / Current Deposit Account or to take
repayment of term deposit on or after maturity. The payment before maturity of term
deposit or loan against term deposit to the survivor/s are not covered by the mandate.
Therefore, to facilitate payment before maturity of term deposit or loan against the same, to
the survivor/s, an authority as under duly signed by all the joint depositors should be
obtained at the time of opening of a term deposit account, which should be kept alongwith
the AOF.
 “In the event of death of Shri_______________________ former, prior to the maturity of the
deposit, the Bank will, at the request of all the surviving depositors, be at liberty, though not
bound and at its absolute discretion (1) to add / delete / substitute any name therein, (2) to
repay the deposit before maturity or (3) to grant an advance against the security thereof, on
such terms as the Bank may in its absolute discretion decide and such repayment before
maturity shall constitute a valid discharge to the Bank.”
3
Note : As the authority as above is not incorporated in the Account Opening Form, the
branches should obtain the same separately from the depositors and attach the same to
the Account Opening Form.
4.6.3 After the death of the former, in case a written request duly signed by all the
surviving depositor/s for addition / deletion / substitution of any name therein is received
by eBoR branches then the concerned branch may in their sole discretion accept or reject
such request.
5. Authorisation:
The Bank has the authority to debit any Accounts to recover any amount credited by the
Bank erroneously.
6. Charges/Fees :
 In Current Deposit Accounts shall be levied as per instructions issued from time to time
which for the present are as under :
6.1 Service Charges to be levied in Current Deposit Accounts with or without ABB facility:
6.1.1 Cheque Book Charges should be recovered in Current Deposit Accounts are
as follows,
Cheque Book charges should be waived, if Minimum Monthly Average Balance in the
account is not less than the following ceilings :
S.
No
Category of Branch Min. Balance / Min.
Monthly Average Balance
1 C.D Accounts at Finacle Branches with ABB facility Rs.1.00 lacs
2 C.D. Accounts at Finacle Branches without ABB
facility and C.D. Accounts at Computerised Branches
Rs.5.00 lacs
3 C.D. Accounts at non-computerised branches at
Metro Centres
Rs.3.00 lacs
4 C.D. Accounts at non-computerised branches at
Rural, Semi-urban and Urban Centres
Rs.2.00 lacs
Note : In case Minimum Monthly Average Balance, as mentioned above, is not maintained
in the Current Deposit Account, Cheque Book Charges at the prescribed rates should be
charged and credited to P&L A/c – Cheque Book Charges.
6.1.2 Attestation of drawer’s signatures on cheques issued to finance companies / other
4
companies – Rs.10/- per attested cheque.
6.1.3 Stop Payment Instructions – Rs.20/- per instrument.
6.1.4 Cheque Returning Charges
(a) In case inward clearing cheque is returned unpaid for reasons of insufficient funds or
exceeding the sanctioned overdraft limit, charges @ Rs. 50/- per instrument, plus actual out
of pocket expenses should be debited to the account.
(b) In case cheque is lodged in clearing & returned for financial reasons, charges @ Rs.20/-
per instrument and interest at the rate applicable for clean overdraft, in case drawings have
been allowed and overdraft is created, should be debited to the account.
6.1.5 Ledger Folio Charges / Incidental Charges to be recovered on half yearly basis :
(a) Rs.60/- per ledger folio at Metro, Urban & Semi Urban eBoR branches with the minimum
of Rs.60/- per half year.
(b) Rs.50/- per ledger folio at Rural eBoR branches with the minimum of Rs.50/- per half
year.
Note : 40 entries or part thereof shall be treated as one ledger folio for a/cs on computers.
(c) However, in the accounts having under noted average credit balance free ledger folios,
per half year, as mentioned against it shall be allowed:
6.1.6 Incidental charges in Inoperative Accounts – as follow
6.1.6.1 Incidental charges in Inoperative Current Deposit Accounts should be
charged at the rates advised by the Bank from time to time which for the present are as
under :
(a) Inoperative Current Deposit Accounts having balance less than Rs.5,000/- Rs.50/- per
half year.
(b) Inoperative Current Deposit Accounts having balance of Rs.5,000/- or more, usual
minimum incidental charges as per para 6.1.7.
16.1.6.2 In cases where by application of incidental charges as per para 6.1.6.1 above, the
balance in the Inoperative Current Deposit Account is likely to become Zero, the
account should be closed by applying incidental charges to the extent of the available
balance.
6.1.7 Charges for not maintaining Minimum Balance as Follows:
5
S.No. Average Credit Balance
1 Upto Rs.25,000/- NIL
2 Above Rs.25,000/- and upto Rs.50,000/-2
3 Above Rs.50,000/- and upto Rs.1.00 lac3
4 Above Rs.1.00 lac and upto Rs.2.00 lacs5
5 Above Rs. 2.00 lacs No limit
No. of free ledger
folios
6.1.7.1 The current account holders are required to maintain a minimum balance in their
accounts as per instructions issued by the Bank from time to time, which for the present
are as under:
Rural
Branches
Semi Urban
Branches
Urban Branches Metro Branches Finacle Branches
Without ABB
Rs.500 Rs.1500 Rs.2500 Rs.5000 Rs.5000
6.1.7.2 As and when the balance in Current Deposit Account at non-computerised
branches goes below the minimum balance required as above, a penalty will be levied as
per instructions issued by the Bank from time to time. For the present the penalty is Rs.50/-
per occasion.
6.1.7.3 In Current Deposit Accounts at computerized branches and in Current
Deposit Accounts without ABB facility at Finacle Branches, if the Quarterly Average Balance
goes below the minimum stipulated in para 3.1 above, penalty should be levied as per
Bank’s instructions in force from time to time, which for the present is Rs.250/- per quarter.
6.1.7.4 The provisions of maintenance of Minimum Balance and levy of charges for nonmaintenance
of Minimum Balance as contained in para Nos. 6.1.7.1, 6.1.7.2 & 6.1.7.3 above
will not apply to
a) Current Deposit Accounts opened prior to 3.8.1995,
c) Current Deposit Accounts enjoying overdraft facility.
6.1.7.5 At Finacle Branches, in Current Deposit Accounts with ABB facility,the
prescribed Quarterly Minimum Average Balance to be maintained at present
is as under :
6.1.7.5.1 Raj Bank Premium Account (RBP) : The customers who opt for ABB facility and
maintain Minimum Quarterly Average Balance (MQAB) of Rs. 1.00 lac are classified under
Raj Bank Premium Account. In case the account holder fails to maintain MQAB of Rs.1.00
lacs, penalty should be levied by the parent branch as under :
(a) MQAB between Rs.75,000/- to Rs. 1.00 lac Rs.250/- per quarter
(b) MQAB between Rs.50,000/- to Rs.75,000/- Rs.500 per quarter
(c) MQAB between Rs.25,000/- to Rs.50,000/- Rs.750/- per quarter
(d) MQAB less than Rs.25,000/- Rs.1,000/- per quarter
6.1.7.5.2. Raj Bank Express Account (RBE) : The customers who opt for ABB facility and
maintain Minimum Quarterly Average Balance (MQAB) of Rs.50,000/- are classified under
6
this category. In case the account holder fails to maintain MQAB of Rs.50,000, penalty
should be levied by the parent branch as under
(a) MQAB between Rs.25,000/- to
Rs.50,000/-
Rs.250/- per quarter
(b) MQAB between Rs.10,000/- to
Rs.25,000/-
Rs.375 per quarter
(c) MQAB less than Rs.10,000/- Rs.500/- per quarter
6.1.7.5.3. Normal Current Account (ABB) : In normal Current Deposit Accounts i.e. other
than Raj Bank Premium Account and Raj Bank Express Account, the customers who opt
for ABB facility are required to maintain a Minimum Quarterly Average Balance
(MQAB) of Rs.10,000/- and in case the account holder fails to maintain MQAB of
Rs.10,000/- penalty should be levied by the parent branch @ Rs.250/- per quarter.
6.1.7.5.4 The charges for non-maintenance of MQAB should not be levied in all types of
Current Deposit Accounts with ABB facility, if term deposit for an equivalent amount in the
same name is deposited. No loan / overdraft against such term deposit/s should be
allowed. However, to distinguish it from other term deposits, kept under lien a noting
to the effect that it is being issued for maintenance of the MQAB in A/c No.___________
should be made on the face of the term deposit receipt.
6.1.7.5.5 Current Deposit Accounts (ABB) with Overdraft Facility :
(a) Overdraft facility against Bank’s own term deposits can be sanctioned in Raj Bank
Premium Accounts and Raj Bank Express Accounts at usual margin stipulated from time to
time provided that the amount of term deposits as security for overdraft is Rs.1,00,000/- or
more in case of Raj Bank Premium Account and Rs.50,000/- or more in case of Raj Bank
Express Account. In Normal Current Deposit Accounts with ABB facility, overdraft facility
should not be allowed to customers. However, in Normal Current Deposit Account with
ABB facility of staff members, overdraft against security of Bank’s own term deposits can
be allowed provided that the amount of term deposits as security for overdraft is
Rs.10,000/- or more.
b) In Raj Bank Premium Account, Raj Bank Express Account and Raj Bank Normal Account
(of staff members), if overdraft facility has been sanctioned / allowed, the account holders
are required to maintain Minimum Quarterly Average Balance, as stipulated in para
6.1.7.5.1, 6.1.7.5.2 and 6.1.7..5.3 above, and in these accounts the Quarterly Average
Balance will be calculated on the basis of the number of days for which the account
remains in credit. If the Quarterly Average Balance in Overdraft Account with ABB facility is
less than the stipulated MQAB, and the avail of overdraft is less than 50% of the sanctioned
limit, the penalty as stipulated in para 6.1.7.5.1, 6.1.7.5.2 and 6.1.7.5.3 herein above should
be charged. (The penalty as stipulated in para 6.1.7.5.1, 6.1.7.5.2 and 6.1.7.5.3 above for
non maintenance of Minimum Quarterly Average Balance may be waived if the availof
overdraft is 50% or more of the sanctioned limit.)
7
c) If the overdraft account remains in debit throughout the quarter, whereby the Quarterly
Average Balance cannot be worked out and the avail is less than 50% of the sanctioned
limit, the penalty for non-maintenance of MQAB should be charged as under :
(i) Rs.1,000/- per quarter in Raj Bank Premium Accounts,
(ii) Rs. 500/- per quarter in Raj Bank Express Accounts and
6.2 Service Charges to be levied in Current Deposit Accounts without ABB Facility :
6.2.1 Issuance of duplicate statement of account / pass book
(a) Rs.20/- per statement of account with last balance only.
(b) Rs.20/- per ledger page or part thereof if previous entries are also to be made.
6.2.2 Standing Instructions
Rs.10/- per transaction in case of credits to another account to upcountry branches or to
another Bank at the same centre. Actual remittance expenses and postage should also be
charged. However, no charges shall be levied for standing instructions involving credits to
account within the same branch such as installments in RSD Account, repayment of term
loan etc.
6.2.3 Closure of Accounts (In case account is closed within one year) – Rs.50/-
Note : Account closure charges shall not be levied on closure of a new a/c within one year,
in case the closure of a/c is due to death of the account holder, transfer of a/c to other
branch of our bank or transfer of the amount to some other a/c in same name at any eBoR
branch.
6.3. Service Charges to be levied in Current Deposit Accounts with ABB Facility :
6.3.1 Intersol Cash Receipt Charges - Intersol Cash Receipt Charges @ Rs.2.50 per
thousand or part thereof with the minimum of Rs.25/- shall be recovered in cash (a) in all
types of Current Deposit Accounts with ABB facility i.e. Raj Bank Premium A/c, Raj Bank
Express Account, Normal Current A/c with ABB and Overdraft A/c with ABB facility, (b) on
entire amount of cash receipt (c) at the time of receipt of cash and (d) by the branch where
cash is deposited.
6.3.2 Intersol Turnover Charges : Turnover charges should be debited quarterly by the
parent branch in all Current Deposit Accounts with ABB facility for all debit and credit
transactions i.e. debit and credit transactions by way of cash, transfer and clearing, @
Re.1/- per thousand with the minimum of Rs.25/- on amount of intersol turnover which is
(a) in excess of 60 times of quarterly average balance (without any ceiling) in a quarter in
Raj Bank Premium Account,
(b) in excess of 45 times of quarterly average balance (without any ceiling) in a quarter in
Raj Bank Express Account and
(c) in excess of 30 times of quarterly average balance or Rs.15.00 lacs whichever is lower,
in a quarter in Normal Current Account (ABB)
8
6.3.3 Intersol Turnover Charges in Overdraft Accounts :
In Raj Bank Premium Account and Raj Bank Express Account with overdraft facility ,
Intersol Turnover charges should be levied as mentioned below. However, in case the
overdraft account remains in debit throughout the quarter, the charges will be Re.1/- per
thousand with the minimum of Rs.25/- for all intersol debit and credit transactions of cash,
transfer & clearing.
Intersol Turnover Charges : Turnover charges should be debited quarterly by the parent
branch in all Current Deposit Accounts with ABB facility for all debit and credit transactions
i.e. debit and credit transactions by way of cash, transfer and clearing, @ Re.1/- per
thousand with the minimum of Rs.25/- on amount of intersol turnover which is
(a) in excess of 60 times of quarterly average balance (without any ceiling) in a quarter in
Raj Bank Premium Account,
(b) in excess of 45 times of quarterly average balance (without any ceiling) in a quarter in
Raj Bank Express Account and
(c) in excess of 30 times of quarterly average balance or Rs.15.00 lacs whichever is lower,
in a quarter in Normal Current Account (ABB)
7. Services:
Various Services may be made available to the Customers by eBOR in connection with the
Account, which shall be subject to these terms and conditions and/ or such other terms
and conditions governing the said Services as may be specifically stipulated by eBOR from
time to time. Notwithstanding anything specified herein such related Services shall be
provided to the Customer at the sole discretion of eBOR. These Terms shall read in addition
to the specific terms and conditions/ agreement (if any) governing the following Services.
Following are the list (not exhaustive) of the Services available to the Customer, in
connection with Account, some of which may be provided only at select branches or
locations and may not be available in all States and cities.
· Multi-City / Payable at Par (PAP) Cheque Facility
· Anywhere Banking Facility
· Doorstep Banking Facility ( Doorstep Banking facility not provided unless specific
 permission of controlling office is obtained.)
· Internet Banking Facility
· Debit / ATM Card
· Mobile Banking
· Cash Management Services (CMS)
· Real Time Gross Settlement (RTGS)
eBOR, may at its sole discretion decide to offer or withdraw certain services to all or some
of the Customer from time to time and eBOR shall not be liable for any losses or damages
incurred by Customers / Potential Customer/s / third parties, in case of provision or
withdrawal of any such services.
9
8. Interest:
No interest shall be payable on the balance maintained in the Account as per directives of
Reserve Bank of India.
9. Death Or Incompetence:
The Customer agrees to notify eBoR branch promptly if any of the joint Account holders or
authorized signatory of the Account dies or is declared incompetent by a court. The eBoR
branch may place a freeze on the Account and stop all operations when any of the joint
Account holders or authorized signatories dies or is declared incompetent. ICICI Bank may
retain the freeze on the Account until it establishes the identity and credentials of the
successor/beneficiary to its satisfaction.
10. Nomination:
Nomination facility is available for Accounts in the names of individuals and proprietorship
firms. Only one nominee is permissible for an Account and the nomination is to be made
by the Customer duly witnessed by a third person. The Customer should ensure that he/it
gets/ is given the acknowledgment as per the nomination rules framed by Reserve Bank of
India. The Customer is at liberty to change the nominee, through declaration in the
appropriate form to revise the nomination during the currency of deposit with ICICI Bank.
Generally, a nomination is valid for all the Accounts under same Customer Identification
number. However, the Customer may have liberty to request for different persons to be
nominees for different Accounts under the same Customer identification number.
11. Sharing Of Information:
The Customer undertakes and authorises the Bank / its Group Companies to exchange,
share or part with all the information, data or documents relating to his/its application to
other ICICI Group Companies/ Banks/ Financial Institutions/ Credit Bureaus/ Agencies/
Statutory Bodies/such other persons as the Bank /its Group Companies may deem
necessary or appropriate as may be required for use or processing of the said information/
data by such person/s or furnishing of the processed information/data/products thereof to
other Banks / Financial Institutions / credit providers / users registered with such persons
and shall not hold the Bank / its Group Companies liable for use of this information.
12. Change Of Terms:
ICICI Bank shall have the absolute discretion to amend or supplement any of the Terms at
any time relating to the Account and/or the Services provided for / in connection with the
same. ICICI Bank may communicate the amended Terms by hosting the same on the
Website or in any other manner as decided by ICICI Bank. The Customer shall be
responsible for regularly reviewing these Terms including amendments thereto as may be
posted on the Website.
13. Non-Transferability:
10
The Account and the Services provided to the Customer are not transferable under any
circumstance and shall be used only by the Customer. However, ICICI Bank shall have the
right to transfer, assign or sell all its rights, benefits or obligations to any person and these
Terms, shall continue to be in force and effect for the benefit of the successors and assigns
of ICICI Bank.
14. Waiver:
No failure or delay by ICICI Bank in exercising any right, power or privilege hereunder shall
operate as a waiver thereof nor shall any single or partial exercise of any other right, power
or privilege constitute as a waiver. The rights and remedies of ICICI Bank as stated herein
shall be cumulative and not exclusive of any rights or remedies provided by law.
15. Force Majeure
ICICI Bank's obligations contained herein will be subject to any occurrence resulting in
prevention from or delay or interruption in performing its obligations if such prevention,
delay or interruption is due to Force Majeure event, [which would include any event
beyond the reasonable control of ICICI Bank, including, without limitation, unavailability of
any communication system, sabotage, fire, flood, explosion, acts of God, civil commotion,
strikes or industrial action of any kind , riots, insurrection, war or acts of government,
changes in legislation and other allied acts of regulatory nature] then ICICI Bank shall not be
deemed to be in default so long as any such cause or the effect thereof persists (provided
that this shall not prevent the accrual of interest on any outstanding amount which would
have been payable but for this provision)and during a reasonable period thereafter within
which any such obligations are not capable of being fulfilled. ICICI Bank shall not be liable
for any action or claim, from any party, arising out of its inability to perform the obligations
for the reasons stated herein.
16. Indemnity:
16.1. The Customer hereby agrees that he/it shall, at his/its own expense, indemnify,
defend and hold harmless ICICI Bank from and against any and all liability, any other loss
that may occur arising from or relating to the operation or use of the Account or the
Services or breach, nonperformance or inadequate performance by the Customer of
any of these Terms or the acts, errors, representations, misrepresentations, misconduct or
negligence of the Customer in performance of its obligations.
16.2. Under no circumstances shall ICICI Bank be liable to the Customer for any direct,
indirect,incidental, consequential, special or exemplary damages in connection with
the Account or the Services.
16.3. ICICI Bank shall not be liable for any failure to perform any obligation contained in
these Terms or for any loss or damage whatsoever suffered or incurred by the Customer
howsoever caused and whether such loss or damage is attributable (directly or
indirectly) to any dispute or any other matter or circumstances whatsoever.
16.4. The Customer shall indemnify ICICI Bank as collecting Banker for any loss or damage
which ICICI Bank may incur or suffer by guaranteeing any endorsement or discharge on a
cheque, bill or other instrument presented for collection and such guarantee as given by
11
ICICI Bank shall be deemed to have been given in every case at the Customer's
express request.
16.5. The Customer shall keep ICICI Bank indemnified at all times against, and save ICICI
Bank harmless from all actions, proceedings, claims, losses, damages, costs,
interest (both before and after judgment) and expenses (including legal costs on a solicitor
and client basis) which may be brought against or suffered or incurred by ICICI Bank in
resolving any dispute relating to the Customer's Account with ICICI Bank or in enforcing
ICICI Bank's rights under or in connection with the Terms and conditions contained herein,
or which may have arisen either directly or indirectly out of or in connection with ICICI Bank
performing its obligations hereunder or accepting instructions, including but not limited to,
fax and other telecommunications or electronic instructions, and acting or failing to act
thereon.
16.6. If any sum due and payable by the Customer is not paid on the due date, including
without limitation any moneys claimed under this Paragraph, the Customer shall be liable
to pay interest (both after as well as before any judgment) on such unpaid sum at such rate
or rates as ICICI Bank may from time to time stipulate from the date the payment is due up
to the date of payment.
16.7. The Customer shall solely be responsible for ensuring full compliance with all the all
the FEMA rules, regulations or notifications thereunder, applicable laws and regulations in
any relevant jurisdiction in connection with establishment of his/her/its relationship with
ICICI Bank and for any/ all the transactions undertaken by the Customer under the various
current account products offered by ICICI Bank and shall indemnify and keep indemnified
ICICI Bank from all actions, proceedings, claims, losses, damages, costs and expenses
(including legal costs on a solicitor and client basis) which may be brought against or
suffered or incurred by ICICI Bank in connection with any failure to comply with any such
applicable laws/regulations.
16.8. The indemnities as aforesaid shall continue notwithstanding the termination of the
Account.
17. No Encumbrances:
The Customer shall not create or permit to subsist, any encumbrance or third party interest
over or against any Account(s) with ICICI Bank or any monies lying therein without ICICI
Bank's prior written consent.
18. The Customer/s shall not associate their name/s with the Bank without the prior
written approval of the Bank.
19. Bankers lien and set off - Marking of lien on deposit / advances accounts
19.1 A banker has a general lien on securities / deposits held by it unless there is a contract,
expressed or implied, to the contrary. The banker’s right of lien is not barred by the law of
limitation which sets a particular time period for filing a suit. As such banker’s lien
continues over the security irrespective of the fact that the period of limitation has expired.
19.2 A banker may, therefore, retain the security. It may be mentioned here that a banker
does not have lien over the credit balance lying in a customer’s SB/CD/CC account. The
12
banker’s right, in such cases is a right of “set off”. The banker’s right of lien can be
exercised on the money lying with him so long as it is earmarked. Where it has ceased to
be such a separate earmarked sum, the banker’s “right of lien” is converted into the “right
of set off”.
19.3 Lien may be marked in the deposit / advances account/s in the following events :
19.3.1 On term deposit receipts / accounts for the purpose of availing advance against
them.
19.3.2 On the term deposit receipt for hiring of locker.
19.3.3 On term deposit receipt for margin on letter of credit / letter of guarantee.
19.3.4 In CC limit lien should be marked for
(a) Invocation of a letter of guarantee
(b) Cheque returned in BP
(c) Release / replacement of securities
(d) Payment under letters of credit
(e) Interest recovery
19.3.5 For any other purpose as per instructions of Branch Manager / Regional Office /
Central Office.
20. Governing Law:
The laws of India shall govern these Terms. The Parties hereby agree that any legal action
or proceedings arising out of the Terms shall be brought in the courts or tribunals at
Mumbai in India and irrevocably submit themselves to the jurisdiction of such courts and
tribunals. ICICI Bank may, however, in its absolute discretion, commence any legal action or
proceedings arising out of the Terms in any other court, tribunal or other appropriate
forum, and the user hereby consents to that jurisdiction. Any provision of the Terms that is
prohibited or unenforceable in any jurisdiction shall, as to such jurisdiction, be ineffective
to the extent of prohibition or unenforceability but shall not invalidate the remaining
provisions of the Terms or affect such provision in any other jurisdiction.
21. Disclosure:
a) The Customer hereby irrevocably authorises the Bank to disclose, as and when the Bank
is required to do so in order to comply with the applicable laws or when the Bank regards
such disclosure as necessary or expedient, (including but not limited to disclosures for the
purpose of credit review of any Account, service/s or credit facilities received by the
Customer from the Bank whether singly or jointly with others or otherwise), any
information relating to the Customer, his/her Account(s) or other assets or credit facilities
whatsoever held on the Customer's behalf to :
· the head office, affiliates, or any other branches or subsidiaries of ICICI Bank
· his/her auditors, professional advisers and any other person(s) under a duty of
13
confidentiality to the Bank;
· vendors, installers, maintainers or servicers of the Bank’s computer systems;
· any exchange, market, or other authority or regulatory body having jurisdiction over the
Bank, its head office or any other branch of ICICI Bank or over any transactions effected by
the Customer or the Customer’s Account;
· any party entitled to make such demand or request;
· any person with whom the Bank contracts or proposes to contract with regard to the sale
or transfer or sharing of any of its rights, obligations or risks under the Terms;
· any person (including any agent, contractor or third party service provider) with whom the
Bank contracts or proposes to contract with regard to the provision of services in respect of
the Customer's Account(s) or Facilities (as the case may be) or in connection with the
operation of the Bank's business;
· any person employed with, or engaged as an agent by, the Bank or its head office or
affiliates, including any relationship officers for the purposes of or in connection with
interactions with the Customers or providing services to the Customers or processing
transactions pertaining to the Customers’ Accounts or Facilities; and
· to enable the Bank to centralise or outsource its data processing and other administrative
operations) to the Bank’s head office, its affiliates or third parties engaged by the Bank for
any such services/operations.
· any government/regulatory/judicial authority/agency in case of default, if any committed
by the Customer in discharge of its / his / her obligation.
· the Customer hereby agrees and consents that the Bank shall be entitled, in connection
with the Customer’s application for any Account, facilities or services provided by the Bank,
or during the course of the Customer’s relationship with the Bank, to obtain and procure
information pertaining to the Customer or any of his/ her/ its Accounts, legal or financial
position from whatever sources available to the Bank.
22. Closer of Current Deposit Account by the Bank.
The Bank has a right to close an account in the following circumstances:
(1) Where the depositor is drawing cheques without providing funds in the account or not
maintaining minimum required balance.
(2) Where the depositor is depositing cheques on another Banks which are not honoured.
(3) Where the depositor frequently request for stop payment of cheques drawn by him.
(4) Where the depositor is trading rashly or fraudulently which transactions are likely to
involve the Bank in a loss.
(5) Where the account is un-remunerative like, deposits of heavy cash in the accounts at
cash surplus branches, large number of transactions in the account without maintaining
corresponding balance in the account etc. """
if t == yes :
    print 'You can move forward in further process'
else :
     print "sorry sir you have to accect it"
    choice = int(raw_input("Enter your choice..."))

    if choice==1 :
        acc_init()
    elif choice==2 :
        acc_dep()
    elif choice==3 :
        acc_withdraw()
