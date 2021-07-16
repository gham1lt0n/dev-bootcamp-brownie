#!/usr/bin/python3
from brownie import PriceExercise, config, network
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
 
 
 
def deploy_price_exercise():
    jobId = config["networks"][network.show_active()]["jobId"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    oracle_address = get_contract("oracle").address
    link_token_address = get_contract("link_token").address
    btc_usd_price_feed_address = get_contract("btc_usd_price_feed").address
    price_exercise = PriceExercise.deploy(
        oracle_address,
        jobId,
        fee,
        link_token_address,
        btc_usd_price_feed_address,
        {"from": account},
        publish_source=get_verify_status(),
    )
    print(f"Price Exercise deployed to {price_exercise.address}")
    return price_exercise
 
 
def main():
    deploy_price_exercise()
