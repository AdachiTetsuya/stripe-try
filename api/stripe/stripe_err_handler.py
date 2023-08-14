import stripe


class StripeHandledError(Exception):
    pass


def stripe_error_handler(e):

    if isinstance(e, stripe.error.RateLimitError):
        raise StripeHandledError("アクセスが集中しています。しばらく待ってから再度お試しください。")

    elif isinstance(e, stripe.error.InvalidRequestError):
        raise StripeHandledError("無効なリクエストです。")

    elif isinstance(e, stripe.error.AuthenticationError):
        raise StripeHandledError("認証に失敗しました。")

    elif isinstance(e, stripe.error.APIConnectionError):
        raise StripeHandledError("現在、取引が実行できない状態にあります。運営にお問い合わせください。")

    else:
        try:
            stripe_error_code_handler(e)
        except StripeHandledError as e:
            raise StripeHandledError(e)


def stripe_error_code_handler(e):
    if hasattr(e, "code"):
        if e.code == "card_declined" and hasattr(e, "decline_code"):
            if e.decline_code in ERROR_CODE_TEXT:
                raise StripeHandledError(DECLINED_CODE_TEXT[e.code])
        if e.code in ERROR_CODE_TEXT:
            raise StripeHandledError(ERROR_CODE_TEXT[e.code])
    raise StripeHandledError(ERROR_CODE_TEXT["other"])


DECLINED_CODE_TEXT = {
    "authentication_required": "この取引には認証が必要なため、カードが拒否されました。再試行しても成功しない場合、お使いのカード発行会社に詳細をご確認ください。",
    "approve_with_id": "支払いをオーソリできません。再試行しても成功しない場合、お使いのカード発行会社に詳細をご確認ください。",
    "card_not_supported": "このカードはこの購入に対応していません。",
    "card_velocity_exceeded": "お客様のカードの残高またはクレジットの利用限度額を超えました。",
    "withdrawal_count_limit_exceeded": "お客様のカードの残高またはクレジットの利用限度額を超えました。",
    "currency_not_supported": "このカードは指定された通貨に対応していません。",
    "duplicate_transaction": "ごく最近に、同一の金額およびクレジットカード情報の取引が送信されています。",
    "expired_card": "カードの有効期限が切れています。",
    "incorrect_number": "カード番号が正しくありません。",
    "invalid_number": "カード番号が正しくありません。",
    "incorrect_cvc": "セキュリティコードが正しくありません。",
    "invalid_cvc": "セキュリティコードが正しくありません。",
    "insufficient_funds": "カードの残高が不足しているため、購入を完了できません。",
    "invalid_account": "お客様のカード、またはカードが連結アカウントが無効です。",
    "new_account_information_available": "お客様のカード、またはカードが連結アカウントが無効です。",
    "invalid_amount": "支払い金額が無効であるか、許容額を超えています。",
    "invalid_expiry_month": "有効期限の月が無効です。",
    "invalid_expiry_year": "有効期限の年が無効です。",
    "issuer_not_available": "支払いをオーソリできませんでした。再試行しても成功しない場合、お使いのカード発行会社に詳細をご確認ください。",
    "not_permitted": "この支払いは許可されていません。",
    "pickup_card": "この支払いにはこのカードを使用できません。",
    "restricted_card": "この支払いにはこのカードを使用できません。",
    "processing_error": "カードの処理中にエラーが発生しました。もう一度支払いを試してください。それでも処理できない場合は、しばらくしてからもう一度試してください。",
    "reenter_transaction": "この支払いは、不明な理由によりカード発行会社によって処理されませんでした。",
    "try_again_later": "カードは不明な理由により拒否されました。もう一度支払いを試してください。",
    "other": "カードは不明な理由により拒否されました。お使いのカード発行会社に詳細をご確認ください。",
}

ERROR_CODE_TEXT = {
    "amount_too_large": "取引額が取引可能な額を超えています。",
    "amount_too_small": "取引額が少なすぎるため、決済を実行できません。",
    "balance_insufficient": "取引額が現在の残高を超えています。",
    "bank_account_declined": "お客様のアカウントでの決済が拒否されました。",
    "bank_account_unusable": "ご使用になったアカウントは利用できません。",
    "bank_account_verification_failed": "お客様のアカウントの認証に失敗しました。",
    "card_decline_rate_limit_exceeded": "お客様のカードは拒否されました。24時間後にこのカードに再度チャージすることができます。",
    "card_declined": DECLINED_CODE_TEXT,
    "debit_not_authorized": "この支払いが不正なものである可能性があります。",
    "expired_card": "カードの有効期限が切れています。",
    "incorrect_cvc": "セキュリティコードが正しくありません。",
    "invalid_cvc": "セキュリティコードが正しくありません。",
    "incorrect_number": "カード番号が正しくありません。",
    "invalid_number": "カード番号が正しくありません。",
    "instant_payouts_unsupported": "お使いのカードはサポートされていません。",
    "insufficient_funds": "カードの残高が不足しているため、購入を完了できません。",
    "invalid_card_type": "使用できないカードのタイプが入力されています。",
    "invalid_characters": "入力された値には、サポートされていない文字が含まれています。",
    "parameter_invalid_integer": "入力された値には、サポートされていない文字が含まれています。",
    "parameter_invalid_string_blank": "入力された値には、サポートされていない文字が含まれています。",
    "parameter_invalid_string_empty": "入力された値には、サポートされていない文字が含まれています。",
    "parameter_unknown": "入力された値には、サポートされていない文字が含まれています。",
    "invalid_charge_amount": "取引額が無効です。",
    "invalid_expiry_month": "有効期限の月が無効です。",
    "invalid_expiry_year": "有効期限の年が無効です。",
    "lock_timeout": "アクセス負荷が大きいため、拒否されました。もう一度、決済を実行してください。",
    "no_account": "存在しないアカウントです。",
    "parameter_invalid_empty": "必要な値が入力されていません。",
    "parameter_missing": "必要な値が入力されていません。",
    "processing_error": "カードの処理中にエラーが発生しました。もう一度支払いを試してください。それでも処理できない場合は、しばらくしてからもう一度試してください。",
    "rate_limit": "アクセスが拒否されました。",
    "refer_to_customer": "カードは不明な理由により拒否されました。お使いのカード発行会社に詳細をご確認ください。",
    "resource_missing": "エラーが発生しました。カード情報を再度登録し直してください。",
    "other": "決済が正しく実行できませんでした。運営にお問い合わせください。",
}
