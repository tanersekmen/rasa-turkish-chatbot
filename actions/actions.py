# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from tradingview_ta import TA_Handler, Interval, Exchange


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_coin_finder"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        coin_finder = tracker.get_slot('coin_finder')
        try:
            coin_name = TA_Handler(
                symbol=coin_finder,    
                screener="crypto",
                exchange="binance",
                interval=Interval.INTERVAL_1_DAY
            )
            output = f"Teknik analiz çıktısı: {coin_name.get_analysis().summary}"
        except: 
            output = 'aradığınız coin maalesef bulunmuyor.'

        dispatcher.utter_message(text=output)
        return []
 
