from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm, PurchaseForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

def inventory(request):
  template = loader.get_template('base.html')
  return HttpResponse(template.render())