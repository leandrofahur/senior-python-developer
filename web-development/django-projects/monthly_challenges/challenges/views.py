from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}


def monthly_challenges_by_number(request, month):
  try:
    months = list(monthly_challenges.keys())
    forward_month = months[month]
    return HttpResponseRedirect(forward_month)
  except:
    return HttpResponseNotFound("<h1>This month is not supported!</h1>")


def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return HttpResponse(challenge_text)
  except:
    return HttpResponseNotFound("<h1>This month is not supported!</h1>")
