from typing import List, Optional
from tinydb import Query
from datetime import datetime
from nutricionist.models import MealEntry
from nutricionist.repositories.base_repository import BaseRepository

class MealEntryRepository(BaseRepository):
  def __init__(self):
    super().__init__()
    self.meal_entry_table = self.get_table('meal_entries')
    
  def create_meal_entry(
    self,
    user_id: int,
    meal_description: str,
    image_path: Optional[str] = None,
    calories: Optional[str] = None,
    carbs: Optional[str] = None,
    proteins: Optional[str] = None,
    fats: Optional[str] = None,
  ) -> MealEntry:
      meal_entry = MealEntry(
        user_id=user_id,
        meal_description=meal_description,
        image_path=image_path,
        calories=calories,
        carbs=carbs,
        proteins=proteins,
        fats=fats,
      )
      self.create_meal_entry_table.insert(meal_entry.model_dump())
      return meal_entry

  def get_meal_entries_by_user_and_date(self, user_id: int, date: datetime) -> List[MealEntry]:
    start_date = datetime.combine(date.date(), datetime.min.time())
    end_date = datetime.combine(date.date(), datetime.max.time())
    
    MealEntryQuery = Query()
    results = self.meal_entry_table.search(
      (MealEntryQuery.user_id == user_id) & 
      (MealEntryQuery.timestamp >= start_date) &
      (MealEntryQuery.timestamp <= end_date) 
    )
    return [MealEntry(**entry) for entry in results]
  
  def update_meal_entry_(self, meal_entry_id: int, **kwargs) -> None:
    MealEntryQuery = Query()
    self.meal_entry_table.update(kwargs, MealEntryQuery.id == meal_entry_id)
    
  def delete_meal_entry(self, meal_entry_id: int) -> None:
    MealEntryQuery = Query()
    self.meal_entry_table.remove(MealEntryQuery.id == meal_entry_id)
    
  def get_all_meal_entries(self) -> List[MealEntry]:
    all_entries = self.meal_entry_table.all()
    return [MealEntry(**entry) for entry in all_entries]
    