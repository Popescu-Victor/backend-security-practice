from fastapi import APIRouter, HTTPException, Depends
from google.cloud.firestore import Client
from app.database import get_db
from app.models import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Client = Depends(get_db)):
    doc_ref = db.collection("items").document()
    doc_ref.set(item.model_dump())
    return ItemResponse(id=doc_ref.id, **item.model_dump())

@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: str, db: Client = Depends(get_db)):
    doc = db.collection("items").document(item_id).get()
    if not doc.exists:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(id=doc.id, **doc.to_dict())

@router.get("/", response_model=list[ItemResponse])
def list_items(db: Client = Depends(get_db)):
    docs = db.collection("items").stream()
    return [ItemResponse(id=doc.id, **doc.to_dict()) for doc in docs]

@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: str, item: ItemCreate, db: Client = Depends(get_db)):
    doc_ref = db.collection("items").document(item_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Item not found")
    doc_ref.update(item.model_dump())
    return ItemResponse(id=item_id, **item.model_dump())

@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: str, db: Client = Depends(get_db)):
    doc_ref = db.collection("items").document(item_id)
    if not doc_ref.get().exists:
        raise HTTPException(status_code=404, detail="Item not found")
    doc_ref.delete()
