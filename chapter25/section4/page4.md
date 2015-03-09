## Modifying the `driver-loop`

Finally, we must change the `driver-loop` procedure (the `read-eval-print`
loop) to use `actual-value` instead of `eval`, so that if a delayed value is
propagated back to the `read-eval-print` loop, it will be forced before being
printed. We also change the prompts to indicate that this is the lazy
evaluator:

    
    (define input-prompt ";;; L-Eval input:")
    (define output-prompt ";;; L-Eval value:")
    (define (driver-loop)
      (prompt-for-input input-prompt)
      (let ((input (read)))
        (let ((output
               (actual-value input the-global-environment)))
          (announce-output output-prompt)
          (user-print output)))
      (driver-loop))
    

