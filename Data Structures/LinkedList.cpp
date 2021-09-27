#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *next;
};

//struct Node *head;
struct Node* insert(struct Node* head,int n);
void disp(struct Node* head);
void remove(struct Node* head,int p);
void rev(struct Node* head);
void recPrint(struct Node *head);
struct Node* recReverse(struct Node* head);
struct Node* insertAtpos(struct Node* head);



int main(){
    struct Node *head=NULL;
    int n,i,x,d;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&x);
        head=insert(head,x);  
    }
    disp(head);
    printf("Position to Delete: ");
    scanf("%d",&d);
    remove(head,d);
    printf("Forward Recursive Printing: \n");
    recPrint(head);
    printf("Recursive Reversing : \n");
    head=recReverse(head);
    disp(head);
    
    return 0;
    
}
struct Node* insert(struct Node* head,int n){
    int i;
    struct Node* temp=(struct Node*)malloc(sizeof(struct Node));
    temp->data=n;
    temp->next=NULL;

    if(head==NULL){
        head=temp;
    }
    else{
        struct Node *temp1=head;
        while(temp1->next!=NULL){
            temp1=temp1->next;
        }
        temp->next=temp1->next;
        temp1->next=temp;
    }
    return head;
}
    void disp(struct Node* head){
        struct Node *temp=head;
        printf("Data in the list: \n");
        while(temp!=NULL){
            
            printf("Data =");
            printf("%d",temp->data);
            printf("\n");
            temp=temp->next;
        }
    }

void remove(struct Node* head,int p){
    printf("After Deleting: \n");
    struct Node *temp1=head;
    if(p==1){
        head=temp1->next;
        disp(head);
        free(temp1);
        return;
    }
    
    int i;
    for(i=0;i<p-2;i++){
        temp1=temp1->next;
    }
    struct Node *temp2=temp1->next;
    temp1->next=temp2->next;
    disp(head);
    free(temp2);
    
}
void rev(struct Node* head){
    printf("After reversing: \n");
    struct Node *current,*prev,*next;
    prev=NULL;
    current=head;

    while (current!=NULL)
    {
        next=current->next;
        current->next=prev;
        prev=current;
        current=next;
    }
    head=prev;
    disp(head);
    
}

struct Node* insertAtpos(struct Node* head,data,n){
    int i;
    struct Node* temp1=(struct Node*) malloc(sizeof(struct Node));
    temp1->data=data;
    temp1->next=NULL;
    if(n==1)
    {
        temp1->next=head;
        head=temp1;
    }
        struct Node* temp2=head;
        for(i=0;i<n-2;i++)
        {
            temp2=temp2->next;
        }
        temp1->next=temp2->next;
        temp2->next=temp1;
    return head;
}
void recPrint(struct Node* p){
    
    if(p==NULL) return;
    printf("%d \n",p->data);
    recPrint(p->next);
    
}

struct Node* recReverse(struct Node* head)
{
    struct Node* p;
    if(head->next == NULL)
    {
        p=head;
        return p;
    }
    
    p=recReverse(head->next);
    struct Node* q=head->next;
    q->next=head;
    head->next=NULL;
    return p;
    
    //return p;
    
}
