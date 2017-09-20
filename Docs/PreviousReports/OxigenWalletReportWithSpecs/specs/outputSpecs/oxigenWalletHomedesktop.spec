@objects
	
	    menu   id   menu
	    sess-cash-back   id   sess-cash-back
	    log-user-name   id   log-user-name
	    isUserLogin   id   isUserLogin
	    mobile   id   mobile
	    mb-rec-sub-loader   id   mb-rec-sub-loader
	    form-mobile-recharge   id   form-mobile-recharge
	    mobprepaid   id   mobprepaid
	    monbpostpaid   id   monbpostpaid
	    mobilerecharge-service_number   id   mobilerecharge-service_number
	    mobilerecharge-operator   id   mobilerecharge-operator
	    service_circle   id   service_circle
	    service_operator   id   service_operator
	    service_operator_alias   id   service_operator_alias
	    mobilerecharge-circle   id   mobilerecharge-circle
	    hidden_is_special   id   hidden_is_special
	    mobilerecharge-amount   id   mobilerecharge-amount
	    mb-rechrge-plans   id   mb-rechrge-plans
	    mb_recharge_sub_container   id   mb_recharge_sub_container
	    button-mobile-recharge   id   button-mobile-recharge
	    mb_recharge_conf_container   id   mb_recharge_conf_container
	    button-mobile-confirm-recharge   id   button-mobile-confirm-recharge
	    frm_btn_skip   id   frm_btn_skip
	    landline   id   landline
	    ll-rec-sub-loader   id   ll-rec-sub-loader
	    form-ll-recharge   id   form-ll-recharge
	    landlinerecharge-operator   id   landlinerecharge-operator
	    service_circle   id   service_circle
	    service_operator   id   service_operator
	    service_operator_alias   id   service_operator_alias
	    bsnl-ll-services   id   bsnl-ll-services
	    landlinerecharge-type   id   landlinerecharge-type
	    landlinerecharge-account_number   id   landlinerecharge-account_number
	    show-bsnl-ll-service-no   id   show-bsnl-ll-service-no
	    landlinerecharge-service_number   id   landlinerecharge-service_number
	    landlinerecharge-circle   id   landlinerecharge-circle
	    lopn   id   lopn
	    landlinerecharge-amount   id   landlinerecharge-amount
	    biller_bill_fetch   id   biller_bill_fetch
	    btn_bbfetch   id   btn_bbfetch
	    land-line-recharge-ca-number   id   land-line-recharge-ca-number
	    landlinerecharge-ca_number   id   landlinerecharge-ca_number
	    ll_recharge_sub_container   id   ll_recharge_sub_container
	    button-ll-recharge   id   button-ll-recharge
	    ll_recharge_conf_container   id   ll_recharge_conf_container
	    button-ll-confirm-recharge   id   button-ll-confirm-recharge
	    frm_btn_skip   id   frm_btn_skip
	    dth   id   dth
	    dth-rec-sub-loader   id   dth-rec-sub-loader
	    form-dth-recharge   id   form-dth-recharge
	    dth_steps   id   dth_steps
	    dthrecharge-service_number   id   dthrecharge-service_number
	    dthrecharge-operator   id   dthrecharge-operator
	    service_circle   id   service_circle
	    service_operator   id   service_operator
	    service_operator_alias   id   service_operator_alias
	    dthrecharge-amount   id   dthrecharge-amount
	    dth_recharge_sub_container   id   dth_recharge_sub_container
	    button-dth-recharge   id   button-dth-recharge
	    dth_recharge_conf_container   id   dth_recharge_conf_container
	    button-dth-confirm-recharge   id   button-dth-confirm-recharge
	    frm_btn_skip   id   frm_btn_skip
	    datacard   id   datacard
	    dc-rec-sub-loader   id   dc-rec-sub-loader
	    form-data-card-recharge   id   form-data-card-recharge
	    mobprepaidd   id   mobprepaidd
	    monbpostpaidd   id   monbpostpaidd
	    dc_steps   id   dc_steps
	    datacardrecharge-service_number   id   datacardrecharge-service_number
	    datacardrecharge-operator   id   datacardrecharge-operator
	    service_circle   id   service_circle
	    service_operator   id   service_operator
	    service_operator_alias   id   service_operator_alias
	    datacardrecharge-circle   id   datacardrecharge-circle
	    datacardrecharge-amount   id   datacardrecharge-amount
	    dc_recharge_sub_container   id   dc_recharge_sub_container
	    button-dc-recharge   id   button-dc-recharge
	    dc_recharge_conf_container   id   dc_recharge_conf_container
	    button-dc-confirm-recharge   id   button-dc-confirm-recharge
	    frm_btn_skip   id   frm_btn_skip
	    gas   id   gas
@on [desktop]


=button-mobile-recharge:=
	button-mobile-recharge:
	    width 47.2% of form-mobile-recharge/width
	    width 271% of mb-rechrge-plans/width
	    width 89.2% of mb_recharge_sub_container/width
	    width 494% of menu/width
	    width 47.2% of mobile/width
	    width 213% of mobilerecharge-amount/width
	    width 100% of mobilerecharge-operator/width
	    width 119% of mobilerecharge-service_number/width
	    height 18% of form-mobile-recharge/height
	    height 97.4% of mb-rechrge-plans/height
	    height 100% of mb_recharge_sub_container/height
	    height 71.2% of menu/height
	    height 18% of mobile/height
	    height 97.4% of mobilerecharge-amount/height
	    height 97.4% of mobilerecharge-operator/height
	    height 97.4% of mobilerecharge-service_number/height
	    inside partly form-mobile-recharge  168px top, 276px right
	    inside partly mb_recharge_sub_container  15px left, 15px right
	    inside partly mobile  168px top, 276px right
	    aligned horizontally bottom form-mobile-recharge
	    aligned horizontally all mb_recharge_sub_container
	    aligned horizontally bottom mobile
	    aligned vertically left form-mobile-recharge
	    aligned vertically right mb-rechrge-plans 1px
	    aligned vertically left mobile
	    aligned vertically right mobilerecharge-service_number 1px
	    left-of mobilerecharge-operator 29px
	    right-of menu 79px
	    below mb-rechrge-plans 20px
	    below menu 413px
	    below mobilerecharge-amount 20px
	    below mobilerecharge-operator 78px
	    below mobilerecharge-service_number 78px
	    centered horizontally inside mb_recharge_sub_container
=form-mobile-recharge:=
	form-mobile-recharge:
	    width 212% of button-mobile-recharge/width
	    width 575% of mb-rechrge-plans/width
	    width 189% of mb_recharge_sub_container/width
	    width 1050% of menu/width
	    width 100% of mobile/width
	    width 451% of mobilerecharge-amount/width
	    width 212% of mobilerecharge-operator/width
	    width 253% of mobilerecharge-service_number/width
	    height 554% of button-mobile-recharge/height
	    height 539% of mb-rechrge-plans/height
	    height 554% of mb_recharge_sub_container/height
	    height 394% of menu/height
	    height 100% of mobile/height
	    height 539% of mobilerecharge-amount/height
	    height 539% of mobilerecharge-operator/height
	    height 539% of mobilerecharge-service_number/height
	    inside partly mobile 
	    aligned horizontally bottom button-mobile-recharge
	    aligned horizontally bottom mb_recharge_sub_container
	    aligned horizontally all mobile
	    aligned vertically left button-mobile-recharge
	    aligned vertically all mobile
	    aligned vertically right mobilerecharge-operator
	    right-of menu 79px
	    below menu 245px
=mb-rechrge-plans:=
	mb-rechrge-plans:
	    width 36.8% of button-mobile-recharge/width
	    width 17.4% of form-mobile-recharge/width
	    width 32.9% of mb_recharge_sub_container/width
	    width 182% of menu/width
	    width 17.4% of mobile/width
	    width 78.4% of mobilerecharge-amount/width
	    width 36.8% of mobilerecharge-operator/width
	    width 44% of mobilerecharge-service_number/width
	    height 103% of button-mobile-recharge/height
	    height 18.5% of form-mobile-recharge/height
	    height 103% of mb_recharge_sub_container/height
	    height 73.1% of menu/height
	    height 18.5% of mobile/height
	    height 100% of mobilerecharge-amount/height
	    height 100% of mobilerecharge-operator/height
	    height 100% of mobilerecharge-service_number/height
	    inside form-mobile-recharge  110px top, 155px left, 277px right, 57px bottom
	    inside mobile  110px top, 155px left, 277px right, 57px bottom
	    aligned horizontally all mobilerecharge-amount
	    aligned vertically right button-mobile-recharge 1px
	    aligned vertically right mobilerecharge-service_number
	    left-of mobilerecharge-operator 30px
	    right-of menu 234px
	    right-of mobilerecharge-amount 0px
	    above button-mobile-recharge 20px
	    above mb_recharge_sub_container 20px
	    below menu 355px
	    below mobilerecharge-operator 20px
	    below mobilerecharge-service_number 20px
=mb_recharge_sub_container:=
	mb_recharge_sub_container:
	    width 112% of button-mobile-recharge/width
	    width 53% of form-mobile-recharge/width
	    width 304% of mb-rechrge-plans/width
	    width 554% of menu/width
	    width 53% of mobile/width
	    width 239% of mobilerecharge-amount/width
	    width 112% of mobilerecharge-operator/width
	    width 134% of mobilerecharge-service_number/width
	    height 100% of button-mobile-recharge/height
	    height 18% of form-mobile-recharge/height
	    height 97.4% of mb-rechrge-plans/height
	    height 71.2% of menu/height
	    height 18% of mobile/height
	    height 97.4% of mobilerecharge-amount/height
	    height 97.4% of mobilerecharge-operator/height
	    height 97.4% of mobilerecharge-service_number/height
	    inside partly form-mobile-recharge  168px top, 261px right
	    inside partly mobile  168px top, 261px right
	    aligned horizontally all button-mobile-recharge
	    aligned horizontally bottom form-mobile-recharge
	    aligned horizontally bottom mobile
	    left-of mobilerecharge-operator 14px
	    right-of menu 64px
	    below mb-rechrge-plans 20px
	    below menu 413px
	    below mobilerecharge-amount 20px
	    below mobilerecharge-operator 78px
	    below mobilerecharge-service_number 78px
	    centered horizontally on button-mobile-recharge
=menu:=
	menu:
	    width 20.2% of button-mobile-recharge/width
	    width 9.56% of form-mobile-recharge/width
	    width 54.9% of mb-rechrge-plans/width
	    width 18.1% of mb_recharge_sub_container/width
	    width 9.56% of mobile/width
	    width 43.1% of mobilerecharge-amount/width
	    width 20.2% of mobilerecharge-operator/width
	    width 24.2% of mobilerecharge-service_number/width
	    height 141% of button-mobile-recharge/height
	    height 25.4% of form-mobile-recharge/height
	    height 137% of mb-rechrge-plans/height
	    height 141% of mb_recharge_sub_container/height
	    height 25.4% of mobile/height
	    height 137% of mobilerecharge-amount/height
	    height 137% of mobilerecharge-operator/height
	    height 137% of mobilerecharge-service_number/height
	    left-of button-mobile-recharge 79px
	    left-of form-mobile-recharge 79px
	    left-of mb-rechrge-plans 234px
	    left-of mb_recharge_sub_container 64px
	    left-of mobile 79px
	    left-of mobilerecharge-amount 118px
	    left-of mobilerecharge-operator 355px
	    left-of mobilerecharge-service_number 118px
	    above button-mobile-recharge 413px
	    above form-mobile-recharge 245px
	    above mb-rechrge-plans 355px
	    above mb_recharge_sub_container 413px
	    above mobile 245px
	    above mobilerecharge-amount 355px
	    above mobilerecharge-operator 297px
	    above mobilerecharge-service_number 297px
=mobile:=
	mobile:
	    width 212% of button-mobile-recharge/width
	    width 100% of form-mobile-recharge/width
	    width 575% of mb-rechrge-plans/width
	    width 189% of mb_recharge_sub_container/width
	    width 1050% of menu/width
	    width 451% of mobilerecharge-amount/width
	    width 212% of mobilerecharge-operator/width
	    width 253% of mobilerecharge-service_number/width
	    height 554% of button-mobile-recharge/height
	    height 100% of form-mobile-recharge/height
	    height 539% of mb-rechrge-plans/height
	    height 554% of mb_recharge_sub_container/height
	    height 394% of menu/height
	    height 539% of mobilerecharge-amount/height
	    height 539% of mobilerecharge-operator/height
	    height 539% of mobilerecharge-service_number/height
	    inside partly form-mobile-recharge 
	    aligned horizontally bottom button-mobile-recharge
	    aligned horizontally all form-mobile-recharge
	    aligned horizontally bottom mb_recharge_sub_container
	    aligned vertically left button-mobile-recharge
	    aligned vertically all form-mobile-recharge
	    aligned vertically right mobilerecharge-operator
	    right-of menu 79px
	    below menu 245px
=mobilerecharge-amount:=
	mobilerecharge-amount:
	    width 47% of button-mobile-recharge/width
	    width 22.2% of form-mobile-recharge/width
	    width 127% of mb-rechrge-plans/width
	    width 41.9% of mb_recharge_sub_container/width
	    width 232% of menu/width
	    width 22.2% of mobile/width
	    width 47% of mobilerecharge-operator/width
	    width 56% of mobilerecharge-service_number/width
	    height 103% of button-mobile-recharge/height
	    height 18.5% of form-mobile-recharge/height
	    height 100% of mb-rechrge-plans/height
	    height 103% of mb_recharge_sub_container/height
	    height 73.1% of menu/height
	    height 18.5% of mobile/height
	    height 100% of mobilerecharge-operator/height
	    height 100% of mobilerecharge-service_number/height
	    inside form-mobile-recharge  110px top, 39px left, 368px right, 57px bottom
	    inside mobile  110px top, 39px left, 368px right, 57px bottom
	    inside partly mb-rechrge-plans  91px right
	    aligned horizontally all mb-rechrge-plans
	    aligned vertically left mobilerecharge-service_number
	    left-of mb-rechrge-plans 0px
	    left-of mobilerecharge-operator 121px
	    right-of menu 118px
	    above button-mobile-recharge 20px
	    above mb_recharge_sub_container 20px
	    below menu 355px
	    below mobilerecharge-operator 20px
	    below mobilerecharge-service_number 20px
=mobilerecharge-operator:=
	mobilerecharge-operator:
	    width 100% of button-mobile-recharge/width
	    width 47.2% of form-mobile-recharge/width
	    width 271% of mb-rechrge-plans/width
	    width 89.2% of mb_recharge_sub_container/width
	    width 494% of menu/width
	    width 47.2% of mobile/width
	    width 213% of mobilerecharge-amount/width
	    width 119% of mobilerecharge-service_number/width
	    height 103% of button-mobile-recharge/height
	    height 18.5% of form-mobile-recharge/height
	    height 100% of mb-rechrge-plans/height
	    height 103% of mb_recharge_sub_container/height
	    height 73.1% of menu/height
	    height 18.5% of mobile/height
	    height 100% of mobilerecharge-amount/height
	    height 100% of mobilerecharge-service_number/height
	    inside partly form-mobile-recharge  52px top, 276px left, 115px bottom
	    inside partly mobile  52px top, 276px left, 115px bottom
	    aligned horizontally all mobilerecharge-service_number
	    aligned vertically right form-mobile-recharge
	    aligned vertically right mobile
	    right-of button-mobile-recharge 29px
	    right-of mb-rechrge-plans 30px
	    right-of mb_recharge_sub_container 14px
	    right-of menu 355px
	    right-of mobilerecharge-amount 121px
	    right-of mobilerecharge-service_number 30px
	    above button-mobile-recharge 78px
	    above mb-rechrge-plans 20px
	    above mb_recharge_sub_container 78px
	    above mobilerecharge-amount 20px
	    below menu 297px
=mobilerecharge-service_number:=
	mobilerecharge-service_number:
	    width 83.8% of button-mobile-recharge/width
	    width 39.6% of form-mobile-recharge/width
	    width 227% of mb-rechrge-plans/width
	    width 74.7% of mb_recharge_sub_container/width
	    width 414% of menu/width
	    width 39.6% of mobile/width
	    width 178% of mobilerecharge-amount/width
	    width 83.8% of mobilerecharge-operator/width
	    height 103% of button-mobile-recharge/height
	    height 18.5% of form-mobile-recharge/height
	    height 100% of mb-rechrge-plans/height
	    height 103% of mb_recharge_sub_container/height
	    height 73.1% of menu/height
	    height 18.5% of mobile/height
	    height 100% of mobilerecharge-amount/height
	    height 100% of mobilerecharge-operator/height
	    inside form-mobile-recharge  52px top, 39px left, 277px right, 115px bottom
	    inside mobile  52px top, 39px left, 277px right, 115px bottom
	    aligned horizontally all mobilerecharge-operator
	    aligned vertically right button-mobile-recharge 1px
	    aligned vertically right mb-rechrge-plans
	    aligned vertically left mobilerecharge-amount
	    left-of mobilerecharge-operator 30px
	    right-of menu 118px
	    above button-mobile-recharge 78px
	    above mb-rechrge-plans 20px
	    above mb_recharge_sub_container 78px
	    above mobilerecharge-amount 20px
	    below menu 297px
