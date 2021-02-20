from flask import render_template, redirect, request, url_for, flash, current_app
from flask_login import login_user, logout_user, login_required, \
    current_user
from . import trans
from .. import db
from ..models import User, AlgorandAccount
from .forms import RegisterAccount
from algosdk.v2client import algod

@trans.route('/account_summary', methods = ['GET'])
def account_summary():
    if current_user.algod_accounts:
        account_list = current_user.algod_accounts
        app = current_app._get_current_object()
        algod_address = app.config['ALGOD_ADDRESS']
        algod_token = ""
        headers = dict()
        headers['X-API-KEY'] = app.config['API_KEY']
        algod_client = algod.AlgodClient(algod_token, algod_address, headers)
        for account in account_list:
            account.refresh(algod_client)
        return render_template('trans/account_summary.html', alist = account_list)
    else:
        flash('Oops! Looks like you have no registered accounts......')
        return redirect(url_for('trans.register'))

@trans.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegisterAccount()
    if form.validate_on_submit():
        if AlgorandAccount.query.filter_by(public_address = form.public_account.data, user_id=current_user.id).all():
            flash("Oops! You have already registered this address!")
        else:
            app = current_app._get_current_object()
            algod_address = app.config['ALGOD_ADDRESS']
            algod_token = ""
            headers = dict()
            headers['X-API-KEY'] = app.config['API_KEY']
            algod_client = algod.AlgodClient(algod_token, algod_address, headers)
            try :
                account_info = algod_client.account_info(form.public_account.data)
                new_account = AlgorandAccount(public_address=form.public_account.data, account_val=account_info.get('amount'), user=current_user)
                db.session.add(new_account)
                db.session.commit()
                flash("Successfully registered address!")
                return redirect(url_for('trans.account_summary'))
            except:
                flash("Oops! There seems to be a problem with the account you submitted......")

    return render_template('trans/register.html', form=form)

@trans.route('/transactions', methods=['GET'])
def recent_transactions():
    if current_user.algod_account:
        account_list = current_user.algod_account
        transaction_list = []
        return render_template('trans/recent_transactions.html')
    else:
        flash('Oops! Looks like you have no registered accounts......')
        return redirect(url_for('trans.register'))
    #
    # if form.validate_on_submit():
    #     algod_address = 'https://testnet-algorand.api.purestake.io/ps2'
    #     algod_token = ""
    #     headers = {
    #         "X-API-Key": "KTDj0s3dSM9LPM1D8mXOUe1XMfmtj1b4eQPkA4A4",
    #     }
    #     algod_client = algod.AlgodClient(algod_token, algod_address, headers)
    #     passphrase = form.mnemonic.data
    #     my_address = mnemonic.to_public_key(passphrase)
    #     account_info = algod_client.account_info(my_address).get('amount')
    #     return render_template('trans/register.html', amount = account_info)
    # return render_template('trans/account_summary.html', form=form)
    #
